# 📚 Student Performance Prediction – End-to-End ML Project

An end-to-end **Machine Learning web application** that predicts **student math scores** based on demographic and academic factors.

The project covers:
- Exploratory Data Analysis (EDA)
- Model Training
- Evaluation
- Deployment using **Flask**

🔗 **Live Demo:**  
👉 https://student-exam-performance-predictor-3.onrender.com


## 🗂️ Project Architecture

Student_Performance_Prediction/
│
├── artifacts/                 # Trained model & preprocessor files
├── notebooks/                 # EDA and experimentation notebooks
├── src/
│   ├── components/            # Data ingestion, transformation, model training
│   ├── pipeline/              # Training and prediction pipelines
│   ├── utils.py               # Utility functions
│   ├── logger.py              # Logging configuration
│   └── exception.py           # Custom exception handling
│
├── templates/                 # HTML templates (Flask)
├── app.py                     # Flask application entry point
├── requirements.txt           # Project dependencies
├── setup.py
└── README.md

## ⚙️ Installation

### 1️⃣ Clone the Repository
    git clone https://github.com/yourusername/student-performance-prediction.git
    cd student-performance-prediction

### 2️⃣ Create & Activate Environment (Optional but Recommended)
    conda create -n student_ml python=3.9 -y
    conda activate student_ml

### 3️⃣ Install Dependencies
    pip install -r requirements.txt


## ▶️ Usage

### Run Data Ingestion
    python src/components/data_ingestion.py

### Run Data Transformation
    python src/components/data_transformation.py

### Train the Model
    python src/components/model_trainer.py

### Run the Flask Application
    python app.py

### Open in Browser
    http://localhost:5000


## 📊 Dataset Information

The dataset contains the following features:

- Gender  
- Race/Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  
- Reading Score  
- Writing Score  

### 🎯 Target Variable

- Math Score  


## 🧠 Model Training & Evaluation

### 🔹 Key Steps

- Data preprocessing & feature engineering  
- Categorical encoding using `ColumnTransformer`  
- Scaling numerical features  
- Training multiple regression models  

### 🔹 Models Used

- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  
- CatBoost Regressor  

### 🔹 Hyperparameter Tuning

- GridSearchCV  

### 🔹 Evaluation Metrics

- R² Score  
- Mean Squared Error (MSE)  

✅ The best-performing model is serialized and used for real-time predictions in the deployed web application.


## 🚀 Deployment

- **Backend:** Flask  
- **Hosting Platform:** Render  
- **Setup:** CI-friendly with `requirements.txt`  

### 🌐 Live Application
👉 https://student-exam-performance-predictor-3.onrender.com  


## 📈 Results & Achievements

- ✔ Built a complete end-to-end ML pipeline  
- ✔ Deployed a production-ready Flask application  
- ✔ Implemented logging & custom exception handling  
- ✔ Solved real-world deployment & dependency issues  
- ✔ Resume-ready, industry-standard project structure  


## 👩‍💻 Author

**Bidisha Biswas**  
Aspiring Data Scientist | ML Engineer  

- 🔗 GitHub: https://github.com/Bidisha03Biswas  
- 🔗 LinkedIn: https://www.linkedin.com/in/bidishabiswas03  
  
