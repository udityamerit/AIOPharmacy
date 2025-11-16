from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from recommender import load_model_components, get_recommendations, get_substitutes
import pandas as pd
import plotly.express as px
import json
import os


# --- App and Login Configuration ---
app = Flask(__name__)
app.secret_key = 'your_super_secret_key_change_this'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'


# --- User Model and Persistent Storage ---
USERS_FILE = 'users.json'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, 'r') as f:
            users_data = json.load(f)
            return {id: User(id, data['username'], data['password']) for id, data in users_data.items()}
    except json.JSONDecodeError:
        print("Error: users.json is corrupted or empty. Creating a new one.")
        return {}
    except Exception as e:
        print(f"Error loading users: {e}")
        return {}


def save_users(users_dict):
    try:
        users_data = {id: {'username': user.username, 'password': user.password} for id, user in users_dict.items()}
        with open(USERS_FILE, 'w') as f:
            json.dump(users_data, f, indent=4)
    except Exception as e:
        print(f"Error saving users: {e}")

users = load_users()

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# --- Load Model Components ---
VECTORIZER_FILE = 'tfidf_vectorizer.pkl'
MATRIX_FILE = 'tfidf_matrix.npz'
DATAFRAME_FILE = 'processed_data.pkl'
vectorizer, matrix, df = load_model_components(VECTORIZER_FILE, MATRIX_FILE, DATAFRAME_FILE)

# --- Route Definitions ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/medicines-showcase')
def medicines_showcase_page():
    if current_user.is_authenticated:
        return redirect(url_for('medicines_page'))
    medicines_sample = []
    
    # --- ENHANCED: Check if dataframe loaded ---
    if df is None or df.empty:
        flash('Sorry, the medicine database is currently unavailable.', 'info')
    else:
        sample_size = min(10, len(df))
        medicines_sample = df.sample(n=sample_size).to_dict('records')
        
    return render_template('medicines_showcase.html', medicines=medicines_sample)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('recommender_page'))
    if request.method == 'POST':
        if 'signup_submit' in request.form:
            username = request.form.get('username')
            password = request.form.get('password')
            
            # --- ENHANCED: Added validation ---
            if not username or not password:
                flash('Username and password are required.', 'danger')
            elif username in [u.username for u in users.values()]:
                flash('Username already exists. Please choose another.', 'danger')
            else:
                new_id = str(len(users) + 1)
                new_user = User(new_id, username, password)
                users[new_id] = new_user
                save_users(users)
                login_user(new_user)
                flash('Account created successfully! You are now logged in.', 'success')
                return redirect(url_for('recommender_page'))
                
        elif 'login_submit' in request.form:
            username = request.form['username_login']
            password = request.form['password_login']
            user = next((u for u in users.values() if u.username == username), None)
            
            if user and user.password == password:
                login_user(user)
                # --- MODIFIED: Redirect to recommender page on login for better UX ---
                flash('Logged in successfully.', 'success')
                return redirect(url_for('recommender_page'))
            else:
                flash('Invalid username or password.', 'danger')
                
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/recommender', methods=['GET', 'POST'])
@login_required
def recommender_page():
    if request.method == 'POST':
        user_query = request.form.get('query')

        # --- ENHANCED: Check if model components are loaded ---
        if df is None or vectorizer is None or matrix is None:
            flash('Sorry, the recommendation service is currently unavailable. Please contact the administrator.', 'danger')
            return render_template('index.html', error="Service unavailable.", query=user_query)

        # --- ENHANCED: Check for empty query ---
        if not user_query or user_query.isspace():
            flash('Please enter a medicine name or a symptom to search.', 'info')
            return render_template('index.html', recommendation=None, error=None, query=None)

        # Get recommendations using the enhanced function
        recommended_medicines = get_recommendations(user_query, df, vectorizer, matrix)
        
        if not recommended_medicines.empty:
            top_recommendation = recommended_medicines.iloc[0].to_dict()
            substitutes = get_substitutes(top_recommendation['name'], df)
            # --- MODIFIED: Pass as records (list of dicts) ---
            other_recommendations = recommended_medicines.iloc[1:].to_dict('records') 
            return render_template('index.html', 
                                   recommendation=top_recommendation, 
                                   substitutes=substitutes, 
                                   other_recommendations=other_recommendations, 
                                   query=user_query)
        
        # --- ENHANCED: More specific error message for "wrong value" ---
        error_message = f"Sorry, we couldn't find any close matches for '{user_query}'. Please check your spelling or try a different term (e.g., 'fever', 'headache')."
        return render_template('index.html', error=error_message, query=user_query)

    # This is for the GET request
    return render_template('index.html', recommendation=None, error=None, query=None)

@app.route('/medicines')
@login_required
def medicines_page():
    # --- ENHANCED: Check if dataframe loaded ---
    if df is None or df.empty:
        flash('Sorry, the medicine database is currently unavailable.', 'danger')
        medicines = []
    else:
        sample_size = min(20, len(df))
        medicines = df.sample(n=sample_size).to_dict('records')
        
    return render_template('medicines.html', medicines=medicines)

@app.route('/contact')
@login_required
def contact_page():
    return render_template('contact.html')

# --- DASHBOARD ROUTE (No changes needed, already has good error handling) ---
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard_page():
    file_path = 'Datasets/final_medicine_dataset_with_age_group.csv'
    
    try:
        df_viz = pd.read_csv(file_path)
    except FileNotFoundError:
        flash('Error: Visualization dataset "final_medicine_dataset_with_age_group.csv" not found in Datasets folder.', 'danger')
        return render_template('dashboard.html', error="Dataset file not found.")
    except Exception as e:
        flash(f'Error loading dataset: {e}', 'danger')
        return render_template('dashboard.html', error=f"Error loading dataset: {e}")

    # Create a set to hold all unique, individual reasons
    unique_reasons_set = set()
    for row in df_viz['reason'].dropna():
        reasons = row.split(',')
        for reason in reasons:
            unique_reasons_set.add(reason.strip())
            
    all_reasons = sorted(list(unique_reasons_set))

    # Initialize variables
    selected_reason = 'All'
    selected_plot_type = 'pie' # Default plot type
    total_medicines = 0
    chart_html = None
    error = None

    if request.method == 'POST':
        selected_reason = request.form.get('reason_filter')
        # Get the plot_type from the form, default to 'pie' if not provided
        selected_plot_type = request.form.get('plot_type', 'pie')

    if selected_reason != 'All':
        df_filtered = df_viz[df_viz['reason'].str.contains(selected_reason, case=False, na=False)]
        
        if df_filtered.empty:
            error = f"No data found for the condition: {selected_reason}"
        else:
            # 1. Calculate the total number of medicines
            total_medicines = len(df_filtered)

            # 2. Prepare data for the age breakdown plot
            age_breakdown = df_filtered.groupby('age_group').size().reset_index(name='Count')
            
            # --- PLOT GENERATION LOGIC ---
            chart_title = f'Age Group Breakdown for "{selected_reason}"'

            if selected_plot_type == 'bar':
                # --- Generate Bar Chart ---
                fig = px.bar(
                    age_breakdown,
                    x='age_group',
                    y='Count',
                    color='age_group',
                    title=chart_title,
                    template='plotly_dark',
                    text='Count' # Add count text to bars
                )
                fig.update_traces(textposition='outside')
                fig.update_layout(xaxis_title='Age Group', yaxis_title='Number of Medicines')
            
            else:
                # --- Generate Pie Chart (Default) ---
                # Create the legend_label column (e.g., "Adult: 150")
                age_breakdown['legend_label'] = age_breakdown.apply(
                    lambda row: f"{row['age_group'].capitalize()}: {row['Count']}", axis=1
                )
                
                fig = px.pie(
                    age_breakdown, 
                    names='legend_label',  # Use the new column for the legend
                    values='Count', 
                    title=chart_title,
                    template='plotly_dark'
                )
                
                # --- THIS IS THE MODIFIED LINE ---
                # Show ONLY the percentage inside the slice
                fig.update_traces(textposition='inside', textinfo='percent')
                # --- END OF MODIFICATION ---

            chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
            
    return render_template(
        'dashboard.html',
        all_reasons=all_reasons,
        selected_reason=selected_reason,
        total_medicines=total_medicines,
        chart_html=chart_html,
        selected_plot_type=selected_plot_type, # Pass this to the template
        error=error
    )
# --- END OF MODIFIED ROUTE ---


if __name__ == '__main__':
    app.run(debug=True)