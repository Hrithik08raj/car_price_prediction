from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pickle
import pandas as pd
import json
import uvicorn
import math

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load the machine learning model
try:
    with open('LinearRegressionModel.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")

# Load valid categories
try:
    with open('categories.json', 'r') as f:
        categories = json.load(f)
        valid_names = categories[0]
        valid_companies = categories[1]
        valid_fuel_types = categories[2]
except Exception as e:
    print(f"Error loading categories: {e}")
    valid_names = []
    valid_companies = []
    valid_fuel_types = []

class PredictionRequest(BaseModel):
    company: str
    name: str
    year: int
    kms_driven: int
    fuel_type: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={
            "companies": valid_companies, 
            "car_models": valid_names, 
            "fuel_types": valid_fuel_types
        }
    )

@app.post("/predict")
async def predict_price(request: PredictionRequest):
    try:
        # The ML model expects a dataframe with these specific columns
        input_data = pd.DataFrame({
            'name': [request.name],
            'company': [request.company],
            'year': [request.year],
            'kms_driven': [request.kms_driven],
            'fuel_type': [request.fuel_type]
        })
        
        prediction = model.predict(input_data)[0]
        
        # Round the price to the nearest integer
        price = math.ceil(max(prediction, 0))
        
        return {"success": True, "prediction": price}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
