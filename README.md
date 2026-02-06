📚 Student Performance Prediction Project

An end-to-end Machine Learning web application that predicts student academic performance (Math score) based on socio-demographic and academic factors.
The project helps identify students who may need additional academic support by leveraging data-driven insights.

🔗 Live Demo (Deployed on Render):
👉 https://student-exam-performance-predictor-3.onrender.com

📑 Table of Contents

📌 Project Overview

🛠️ Tech Stack

🗂️ Project Architecture

⚙️ Installation

▶️ Usage

📊 Dataset Information

🧠 Model Training and Evaluation

🚀 Deployment

📈 Results

👩‍💻 Contributors

📌 Project Overview

This project builds a complete Machine Learning pipeline, starting from raw data ingestion to model deployment.
Multiple regression models are trained and evaluated to predict student math scores using features such as parental education, test preparation, and reading/writing scores.

The final model is exposed via a Flask web application and deployed on Render, making it accessible through a public URL for real-time predictions.

🛠️ Tech Stack

Programming Language: Python

Libraries: Pandas, NumPy, scikit-learn

Machine Learning Models:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Support Vector Regressor (SVR)

XGBoost

CatBoost

Model Serialization: dill

Backend Framework: Flask

Deployment Platform: Render

Version Control: Git & GitHub

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

Follow the steps below to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/yourusername/student-performance-prediction.git
cd student-performance-prediction
2️⃣ Create and Activate Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Usage
Run Data Ingestion
python src/components/data_ingestion.py
Run Data Transformation
python src/components/data_transformation.py
Train the Model
python src/components/model_trainer.py
Run the Flask Application
python app.py

Open your browser and navigate to:

http://localhost:5000
📊 Dataset Information

The dataset contains information related to students’ academic background and performance.

🔹 Features

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

The machine learning workflow includes:

Data preprocessing and cleaning

Encoding categorical variables using ColumnTransformer

Feature scaling

Training multiple regression models

Hyperparameter tuning using GridSearchCV

Model evaluation using:

R² Score

Mean Squared Error (MSE)

The best-performing model is serialized and used for prediction in the deployed application.

🚀 Deployment

Backend built using Flask

Hosted on Render

Publicly accessible via browser

🔗 Live Application:
👉 https://student-exam-performance-predictor-3.onrender.com

⚠️ Note: Render free tier may take a few seconds to wake up on the first request.

📈 Results

Successfully built and deployed an end-to-end ML application

Achieved strong predictive performance on unseen test data

Implemented robust logging and custom exception handling

Solved real-world deployment challenges related to dependency versions

👩‍💻 Contributors

Bidisha Biswas
