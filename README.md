📚 Student Performance Prediction Project

An end-to-end **Machine Learning web application** that predicts student academic performance (Math score) based on socio-demographic and academic factors.  
The project helps identify students who may need additional academic support by leveraging data-driven insights.

🔗 **Live Demo (Deployed on Render):**  
👉 https://student-exam-performance-predictor-3.onrender.com


📑 Table of Contents
- Project Overview
- Tech Stack
- Project Architecture
- Installation
- Usage
- Dataset Information
- Model Training and Evaluation
- Deployment
- Results
- Contributors


📌 Project Overview

This project builds a complete **ML pipeline** starting from raw data ingestion to model deployment.  
Multiple regression models are trained and evaluated to predict **student math scores** using features such as parental education, test preparation, and reading/writing scores.

The final model is exposed via a **Flask web application** and deployed on **Render**, making it accessible through a public URL.


🛠️ Tech Stack

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, scikit-learn
- **ML Models:**
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - Support Vector Regressor (SVR)
  - XGBoost
  - CatBoost
- **Model Serialization:** dill
- **Backend Framework:** Flask
- **Deployment:** Render
- **Version Control:** Git & GitHub


🗂️ Project Architecture
Student_Performance_Prediction/
│
├── artifacts/                  # Trained model & preprocessor files
├── notebooks/                  # EDA and experimentation notebooks
├── src/
│   ├── components/             # Data ingestion, transformation, model training
│   ├── pipeline/               # Training and prediction pipelines
│   ├── utils.py                # Utility functions
│   ├── logger.py               # Logging configuration
│   └── exception.py            # Custom exception handling
│
├── templates/                  # HTML templates (Flask)
├── app.py                      # Flask application entry point
├── requirements.txt            # Project dependencies
├── setup.py
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/student-performance-prediction.git
cd student-performance-prediction

Install dependencies:

pip install -r requirements.txt
▶️ Usage

Run data ingestion:

python src/components/data_ingestion.py

Run data transformation:

python src/components/data_transformation.py

Train the model:

python src/components/model_trainer.py

Run the Flask app:

python app.py

Open in browser:

http://localhost:5000
📊 Dataset Information

The dataset includes the following features:

Gender

Race/Ethnicity

Parental Level of Education

Lunch Type

Test Preparation Course

Reading Score

Writing Score

🎯 Target Variable

Math Score

🧠 Model Training and Evaluation

Data preprocessing and feature engineering

Encoding categorical variables using ColumnTransformer

Training multiple regression models

Hyperparameter tuning using GridSearchCV

Evaluation using:

R² Score

Mean Squared Error (MSE)

The best-performing model is saved and used for prediction in the deployed application.

🚀 Deployment

The application is deployed using Flask and hosted on Render.

Live URL:
👉 https://student-exam-performance-predictor-3.onrender.com

📈 Results

Built a full end-to-end ML application

Achieved strong performance on unseen test data

Implemented logging and custom exception handling

Successfully resolved deployment and dependency issues

👩‍💻 Contributors

Bidisha Biswas
