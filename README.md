# AIOPharmacy 🏥💊

<div align="center">

![AIOPharmacy Logo](static/doc.gif)

### Intelligent Medicine Recommendation System Powered by AI

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**[View Demo](#-live-demo) · [Report Bug](https://github.com/udityamerit/AIOPharmacy/issues) · [Request Feature](https://github.com/udityamerit/AIOPharmacy/issues)**

</div>

---

## 📑 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Machine Learning Model](#-machine-learning-model)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 About The Project

**AIOPharmacy** is an advanced, AI-powered medicine recommendation system designed to revolutionize how users discover and learn about medications. Built with cutting-edge Natural Language Processing (NLP) techniques, this platform analyzes symptoms, medicine names, and medical conditions to provide accurate, instant recommendations.

### 🌟 Vision

To democratize access to pharmaceutical information and empower individuals to make informed healthcare decisions through intelligent technology.

### 💡 Problem Statement

- **Information Overload**: Difficulty finding the right medicine among thousands of options
- **Symptom Matching**: Challenges in identifying appropriate medications based on symptoms
- **Alternative Discovery**: Limited knowledge about substitute medicines and brand alternatives
- **Accessibility**: Need for instant, reliable pharmaceutical information

### ✅ Solution

AIOPharmacy leverages **TF-IDF vectorization** and **Cosine Similarity algorithms** to create an intelligent recommendation engine that:
- Matches symptoms to appropriate medications with high accuracy
- Provides comprehensive medicine information and alternatives
- Delivers instant results through an intuitive interface
- Offers voice-enabled search for enhanced accessibility

---

## 🚀 Key Features

### 🔍 **Intelligent Search Engine**
- **Symptom-Based Recommendations**: Enter symptoms like "fever and headache" to get relevant medicines
- **Medicine Name Search**: Find similar alternatives to any medication
- **Smart Matching Algorithm**: Uses NLP to understand context and provide accurate results
- **Threshold-Based Filtering**: Only shows medicines above similarity threshold for quality results

### 🎤 **Voice Recognition**
- **Speech-to-Text**: Speak your symptoms instead of typing
- **Real-Time Visualization**: Audio wave visualization during voice input
- **Multi-Language Support**: Recognizes multiple accents and dialects
- **Browser-Based**: No additional software required

### 📊 **Med Analyzer Dashboard**
- **Interactive Visualizations**: Dynamic Plotly charts (Pie & Bar)
- **Condition-Based Filtering**: Analyze medicines by medical conditions
- **Age Group Analysis**: View distribution across different age demographics
- **Statistical Insights**: Total medicine counts and detailed breakdowns

### 💊 **Comprehensive Medicine Database**
- **Detailed Information**: Name, description, usage, age groups
- **Brand Substitutes**: Up to 5 alternative brands per medicine
- **Similar Medicines**: Discover related medications
- **Regular Updates**: Expandable database structure

### 🔐 **Multi-Role Authentication**
- **Secure Login System**: Password hashing and session management
- **Role-Based Access**: Users, Pharmacists, Hospitals, Vendors
- **Persistent Storage**: JSON-based user data management
- **Session Security**: Flask-Login integration

### 📧 **Communication Platform**
- **Contact System**: EmailJS-powered messaging
- **User Feedback**: Direct communication channel
- **Support Integration**: Easy query submission

---

## 🛠️ Technology Stack

### **Backend Technologies**

| Technology | Purpose | Version |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core Language | 3.8+ |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) | Web Framework | 2.0+ |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data Processing | Latest |
| ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) | Machine Learning | Latest |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) | Numerical Computing | Latest |
| ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white) | Scientific Computing | Latest |

### **Frontend Technologies**

| Technology | Purpose |
|------------|---------|
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) | Structure |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) | Styling |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) | Interactivity |
| ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white) | Data Visualization |

### **Libraries & APIs**
- **Particles.js**: Animated background effects
- **Web Speech API**: Voice recognition functionality
- **EmailJS**: Email integration
- **Font Awesome**: Icon library
- **Google Fonts**: Typography (Poppins)

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[User Interface] --> B[Flask Application]
    B --> C[Authentication System]
    B --> D[Recommendation Engine]
    B --> E[Dashboard Analytics]
    
    D --> F[TF-IDF Vectorizer]
    D --> G[Cosine Similarity]
    F --> H[Medicine Database]
    G --> H
    
    E --> I[Plotly Visualization]
    I --> H
    
    C --> J[User Storage JSON]
    
    style A fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff
    style B fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff
    style D fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff
    style H fill:#f39c12,stroke:#e67e22,stroke-width:2px,color:#fff
```

### **Data Flow**

```
User Input (Symptoms/Medicine Name)
        ↓
Text/Voice Processing
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity Calculation
        ↓
Similarity Scoring & Ranking
        ↓
Top-10 Medicine Recommendations
        ↓
Display with Substitutes & Details
```

---

## 🎬 Getting Started

### **Prerequisites**

Before you begin, ensure you have the following installed:

```bash
Python 3.8 or higher
pip (Python package installer)
Git
```

### **Installation**

Follow these steps to set up the project locally:

#### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/udityamerit/AIOPharmacy.git
cd AIOPharmacy
```

#### 2️⃣ **Create Virtual Environment** (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

#### 4️⃣ **Prepare Dataset**

Ensure the dataset is in the correct location:

```
AIOPharmacy/
└── Datasets/
    └── final_medicine_dataset_with_age_group.csv
```

#### 5️⃣ **Train the Machine Learning Model**

```bash
python train_model.py
```

**Expected Output:**
```
--- Starting Model Training ---
Step 1/4: Loading and preprocessing data...
Data loaded successfully.
Step 2/4: Training the NLP model (TfidfVectorizer)...
NLP model trained.
Step 3/4: Saving the vectorizer to tfidf_vectorizer.pkl...
Vectorizer saved.
Step 4/4: Saving the TF-IDF matrix to tfidf_matrix.npz and data to processed_data.pkl...
Matrix and data saved.

--- Training Complete! ---
```

#### 6️⃣ **Configure Application**

Update security settings in `app.py`:

```python
app.secret_key = 'your_unique_secret_key_here'
```

Update EmailJS credentials in `templates/contact.html`:

```javascript
emailjs.init("YOUR_EMAILJS_USER_ID");
const serviceID = 'YOUR_SERVICE_ID';
const templateID = 'YOUR_TEMPLATE_ID';
```

#### 7️⃣ **Run the Application**

```bash
python app.py
```

#### 8️⃣ **Access the Application**

Open your browser and navigate to:
```
http://localhost:5000
```

---

## 📖 Usage Guide

### **For End Users**

#### **1. Creating an Account**
1. Navigate to the login page
2. Select your role (User/Pharmacist/Hospital/Vendor)
3. Click "Sign Up" and enter credentials
4. You'll be automatically logged in

#### **2. Searching for Medicines**

**Method 1: Text Search**
```
1. Go to "Recommender" page
2. Type symptoms or medicine name
3. Click "Search" or press Enter
4. View top recommendation with alternatives
```

**Method 2: Voice Search**
```
1. Click the microphone icon
2. Speak your symptoms clearly
3. System automatically processes and searches
4. Results appear instantly
```

#### **3. Viewing Analytics**
```
1. Navigate to "Med Analyzer"
2. Select a medical condition from dropdown
3. Click "Analyze"
4. View total medicines and age distribution
5. Toggle between Pie and Bar charts
```

### **For Developers**

#### **Adding New Medicines**
Update your CSV file and retrain:
```bash
python train_model.py
```

#### **Adjusting Similarity Threshold**
Edit `recommender.py`:
```python
SIMILARITY_THRESHOLD = 0.1  # Increase for stricter matching
```

#### **Customizing UI**
Edit `static/style.css` for styling changes.

---

## 📡 API Documentation

### **Endpoints**

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/` | GET | ❌ | Landing page |
| `/login` | GET, POST | ❌ | Authentication |
| `/logout` | GET | ✅ | User logout |
| `/recommender` | GET, POST | ✅ | Medicine search |
| `/medicines` | GET | ✅ | Browse medicines |
| `/medicines-showcase` | GET | ❌ | Public preview |
| `/dashboard` | GET, POST | ✅ | Analytics |
| `/contact` | GET | ✅ | Contact form |

### **Request Examples**

#### **Medicine Search (POST /recommender)**

```python
POST /recommender
Content-Type: application/x-www-form-urlencoded

query=fever+and+headache
```

**Response:**
```json
{
  "recommendation": {
    "name": "Paracetamol",
    "description": "Pain reliever and fever reducer",
    "reason": "Fever, Pain, Headache",
    "age_group": "Adult"
  },
  "substitutes": ["Crocin", "Dolo", "Calpol", "Tylenol"],
  "other_recommendations": [...]
}
```

---

## 📂 Project Structure

```
AIOPharmacy/
│
├── 📄 app.py                           # Main Flask application
├── 📄 recommender.py                   # ML recommendation engine
├── 📄 train_model.py                   # Model training script
├── 📄 requirements.txt                 # Python dependencies
├── 📄 README.md                        # Project documentation
├── 📄 LICENSE                          # MIT License
│
├── 📁 Datasets/
│   └── final_medicine_dataset_with_age_group.csv
│
├── 📁 static/                          # Static assets
│   ├── style.css                       # Main stylesheet
│   ├── doc.gif                         # Animated doctor
│   └── scanning.gif                    # Search animation
│
├── 📁 templates/                       # HTML templates
│   ├── base.html                       # Base template
│   ├── home.html                       # Landing page
│   ├── login.html                      # Authentication
│   ├── index.html                      # Recommender interface
│   ├── dashboard.html                  # Analytics dashboard
│   ├── medicines.html                  # Medicine catalog
│   ├── medicines_showcase.html         # Public preview
│   └── contact.html                    # Contact form
│
├── 📁 Model Files/ (Generated)
│   ├── tfidf_vectorizer.pkl           # Trained vectorizer
│   ├── tfidf_matrix.npz               # TF-IDF matrix
│   └── processed_data.pkl             # Processed dataset
│
└── 📄 users.json (Generated)          # User data storage
```

---

## 🧠 Machine Learning Model

### **Algorithm Overview**

#### **TF-IDF (Term Frequency-Inverse Document Frequency)**

TF-IDF converts text into numerical features by considering:
- **Term Frequency (TF)**: How often a term appears in a document
- **Inverse Document Frequency (IDF)**: How unique a term is across all documents

**Formula:**
```
TF-IDF(t, d) = TF(t, d) × IDF(t)

where:
TF(t, d) = (Number of times term t appears in document d) / (Total terms in document d)
IDF(t) = log(Total documents / Documents containing term t)
```

#### **Cosine Similarity**

Measures similarity between two vectors using the cosine of the angle between them.

**Formula:**
```
similarity = (A · B) / (||A|| × ||B||)

where:
A · B = dot product of vectors A and B
||A||, ||B|| = magnitude of vectors A and B
```

**Range**: 0 (completely different) to 1 (identical)

### **Implementation Details**

#### **Data Preprocessing**
```python
# Combine relevant fields into 'soup'
df['soup'] = df['name'] + ' ' + df['description'] + ' ' + df['reason']

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['soup'])
```

#### **Recommendation Process**
```python
# Transform user query
query_vec = vectorizer.transform([user_query])

# Calculate similarities
cosine_similarities = cosine_similarity(query_vec, tfidf_matrix)

# Get top matches above threshold
top_matches = similarities[similarities > THRESHOLD]
```

### **Model Performance**

- **Dataset Size**: 10,000+ medicines
- **Feature Dimensions**: ~5,000 unique terms
- **Average Response Time**: <500ms
- **Similarity Threshold**: 0.1 (configurable)
- **Top Recommendations**: 10 per query

---

## 📸 Screenshots

### Landing Page
*Modern, animated landing page with particle effects*

### Medicine Recommender
*Intelligent search with voice recognition*

### Analytics Dashboard
*Interactive visualizations with filtering options*

### Mobile Responsive
*Fully responsive design across all devices*

> **Note**: Add actual screenshots to your repository in a `/screenshots` folder

---

## 🗺️ Roadmap

### **Phase 1: Core Features** ✅
- [x] Basic recommendation engine
- [x] User authentication
- [x] Voice recognition
- [x] Analytics dashboard

### **Phase 2: Enhancements** 🚧
- [ ] Advanced filtering options
- [ ] User review system
- [ ] Medicine interaction warnings
- [ ] Prescription upload feature
- [ ] Multi-language support

### **Phase 3: Advanced Features** 📋
- [ ] AI chatbot integration
- [ ] Doctor consultation booking
- [ ] Pharmacy locator
- [ ] Mobile application (React Native)
- [ ] Blockchain for prescription verification

### **Phase 4: Enterprise** 🔮
- [ ] Hospital management system integration
- [ ] Insurance claim processing
- [ ] Telemedicine platform
- [ ] API for third-party integrations

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### **How to Contribute**

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### **Contribution Guidelines**

- Follow PEP 8 style guide for Python code
- Write clear, descriptive commit messages
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting PR

### **Code of Conduct**

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

```
MIT License

Copyright (c) 2024 Uditya Narayan Tiwari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👤 Contact

**Uditya Narayan Tiwari**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/uditya-narayan-tiwari-562332289/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/udityamerit)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)

**Project Link**: [https://github.com/udityamerit/AIOPharmacy](https://github.com/udityamerit/AIOPharmacy)

---

## 🙏 Acknowledgments

### **Inspiration & Resources**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Plotly Documentation](https://plotly.com/python/)
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

### **Special Thanks**
- Open-source community for amazing libraries
- Medical professionals for domain knowledge
- Beta testers for valuable feedback

### **Libraries & Tools**
- Particles.js for background animations
- Font Awesome for icons
- Google Fonts for typography
- EmailJS for email integration

---

## ⚠️ Disclaimer

**IMPORTANT MEDICAL DISCLAIMER:**

This application is designed for **educational and informational purposes only**. The medicine recommendations provided by AIOPharmacy should NOT be considered as professional medical advice, diagnosis, or treatment.

**Key Points:**
- ✋ Always consult qualified healthcare professionals before taking any medication
- 🏥 Never replace professional medical consultation with application recommendations
- 💊 Medication effects vary by individual health conditions
- ⚕️ Self-medication can be dangerous without proper medical supervision
- 📞 In case of medical emergency, contact emergency services immediately

**By using this application, you acknowledge that:**
1. The recommendations are algorithmically generated
2. They may not account for drug interactions or allergies
3. You take full responsibility for any medical decisions
4. The developers are not liable for any health consequences

**For Medical Emergencies:** Call your local emergency number immediately.

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/udityamerit/AIOPharmacy?style=social)
![GitHub forks](https://img.shields.io/github/forks/udityamerit/AIOPharmacy?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/udityamerit/AIOPharmacy?style=social)
![GitHub issues](https://img.shields.io/github/issues/udityamerit/AIOPharmacy)
![GitHub pull requests](https://img.shields.io/github/issues-pr/udityamerit/AIOPharmacy)

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ by Uditya Narayan Tiwari**

[Back to Top](#aiopharmacy-)

</div>
