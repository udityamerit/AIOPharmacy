import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from scipy.sparse import load_npz
import os

# --- NEW: Added a threshold for minimum similarity ---
SIMILARITY_THRESHOLD = 0.2 # Adjust this value (0.0 to 1.0) as needed

def load_model_components(vectorizer_path, matrix_path, df_path):
    """
    Loads the pre-trained model components from disk.
    """
    print("--- Initializing Recommender ---")
    if not all(os.path.exists(p) for p in [vectorizer_path, matrix_path, df_path]):
        print("\nFATAL ERROR: Model components not found.")
        print("Please run 'train_model.py' first to train the model and create the necessary files.")
        return None, None, None

    try:
        with open(vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)
        matrix = load_npz(matrix_path)
        df = pd.read_pickle(df_path)
        print("Recommender initialized successfully.")
        return vectorizer, matrix, df
    except Exception as e:
        print(f"\nERROR loading model components: {e}")
        return None, None, None

def get_recommendations(query, df, vectorizer, matrix):
    """
    Gets medicine recommendations based on a query using TF-IDF cosine similarity.
    This searches the 'soup' (name, description, and reason).
    """
    # --- MODIFIED: Removed direct search, now only uses cosine similarity ---
    
    # 1. Transform the user query
    query_vec = vectorizer.transform([query])
    
    # 2. Calculate cosine similarity
    cosine_sim = cosine_similarity(query_vec, matrix).flatten()
    
    # 3. Get similarity scores with their indices
    sim_scores = list(enumerate(cosine_sim))
    
    # 4. Sort medicines based on similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # --- NEW: Check if the top match is above the threshold ---
    if not sim_scores or sim_scores[0][1] < SIMILARITY_THRESHOLD:
        # If no match is good enough, return an empty DataFrame
        return pd.DataFrame() 

    # --- MODIFIED: Get top 10 results (changed from [1:11] to [0:10]) ---
    sim_scores = sim_scores[0:10]
    
    # 6. Get the medicine indices
    medicine_indices = [i[0] for i in sim_scores]
    
    # 7. Return the top 10 most similar medicines
    return df.iloc[medicine_indices]

def get_substitutes(medicine_name, df):
    """
    Gets substitutes for a given medicine.
    """
    substitutes = df[df['name'] == medicine_name][['substitute0', 'substitute1', 'substitute2', 'substitute3', 'substitute4']]
    return substitutes.values.flatten().tolist()

if __name__ == '__main__':
    # --- Load Model Components ---
    VECTORIZER_FILE = 'tfidf_vectorizer.pkl'
    MATRIX_FILE = 'tfidf_matrix.npz'
    DATAFRAME_FILE = 'processed_data.pkl'

    vectorizer, matrix, df = load_model_components(VECTORIZER_FILE, MATRIX_FILE, DATAFRAME_FILE)

    if df is not None:
        # --- Get Recommendations (Example: by reason) ---
        query = "Fever and Pain"
        recommendations = get_recommendations(query, df, vectorizer, matrix)
        print(f"\nRecommendations for '{query}':")
        print(recommendations[['name', 'description', 'reason']])
        
        # --- Get Recommendations (Example: by name) ---
        query_name = "Paracetamol"
        recommendations_name = get_recommendations(query_name, df, vectorizer, matrix)
        print(f"\nRecommendations for '{query_name}':")
        print(recommendations_name[['name', 'description', 'reason']])


        # --- Get Substitutes ---
        if not recommendations_name.empty:
            medicine_name = recommendations_name.iloc[0]['name']
            substitutes = get_substitutes(medicine_name, df)
            print(f"\nSubstitutes for '{medicine_name}':")
            print(substitutes)