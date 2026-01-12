from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import LaptopData
from model.predict import model_loaded, MODEL_VERSION, predict_price

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Welcome to Laptop Price Predictor!'}

@app.get("/health")
def health_check():
    return {
        'status': 'OK',
        'model_loaded': model_loaded is not None,
        'version': MODEL_VERSION
    }

@app.post("/predict")
def get_price(laptop_data:LaptopData):
    try:
        # pass the data into predict_price
        prediction = predict_price(laptop_data)

        # return the predicted_price
        return JSONResponse(status_code=200, content=prediction)
    except Exception as e:
        # some error occurred
        return JSONResponse(status_code=500, content=str(e))