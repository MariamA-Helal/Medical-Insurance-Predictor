# Medical-Insurance-Predictor

#  Medical Insurance Cost Predictor

This is a Full-Stack Machine Learning web application that predicts medical insurance premiums based on user demographics and health factors.

##  Features
- **Accurate Prediction:** Uses a trained Machine Learning model (Random Forest/Linear Regression).
- **Interactive UI:** Clean and responsive web interface built with HTML and Bootstrap.
- **FastAPI Backend:** High-performance API handling data processing and model inference.
- **Automated Insights:** Provides instant medical analysis and health tips based on input data.

##  Tech Stack
- **Backend:** FastAPI (Python)
- **Machine Learning:** Scikit-Learn, Pandas, Joblib
- **Frontend:** HTML5, CSS3, Bootstrap
- **Server:** Uvicorn

##  How to Run
1. Clone the repository.
2. Install requirements: `pip install -r requirements.txt`
3. Start the server: `uvicorn main:app --reload`
4. Open your browser at `http://127.0.0.1:8000`

##  Model Factors
The model considers the following features:
- Age, BMI, Gender, Smoking Status, Number of Children, and Region.
