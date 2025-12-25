from http.client import responses
from fastapi import FastAPI, Form, Request
import joblib
import os
import pandas as pd
import g4f
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'insurance_model.pkl')
model = joblib.load(model_path)

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})


@app.post("/predict")
async def predict_insurance(request: Request, age: int = Form(...), bmi: float = Form(...),
                            children: int = Form(...), sex: str = Form(...),
                            smoker: str = Form(...), region: str = Form(...)):
    
    model_path = os.path.join(BASE_DIR, 'insurance_model.pkl')
    model = joblib.load(model_path)


    is_male = 1 if sex.lower() == "male" else 0
    is_smoker = 1 if smoker.lower() == "yes" else 0
    r_nw = 1 if region == "northwest" else 0
    r_se = 1 if region == "southeast" else 0
    r_sw = 1 if region == "southwest" else 0

    input_data = pd.DataFrame([[age, bmi, children, is_male, is_smoker, r_nw, r_se, r_sw]],
                              columns=['age', 'bmi', 'children', 'sex_male', 'smoker_yes',
                                       'region_northwest', 'region_southeast', 'region_southwest'])


    prediction = model.predict(input_data)[0]

    analysis_parts = []

    if smoker.lower() == "yes":
        analysis_parts.append("Smoking is the primary factor increasing your cost.")
    else:
        analysis_parts.append("Great job being a non-smoker; this helps keep your rates lower.")

    if bmi > 25:
        analysis_parts.append("Your BMI is above the ideal range, which adds to the premium.")
    else:
        analysis_parts.append("Your BMI is within a healthy range.")

    if age > 45:
        analysis_parts.append("Age-related adjustments are applied to this estimate.")

    ai_msg = " ".join(analysis_parts)

    return {
        "Predicted_Cost": f"{round(prediction, 2)}$",
        "Analysis": ai_msg

    }
