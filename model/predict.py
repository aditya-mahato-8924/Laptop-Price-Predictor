import pandas as pd
import numpy as np
import pickle
from schema.user_input import LaptopData

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

model_loaded = True if model else False
MODEL_VERSION = '1.0.0' # version of the model

def predict_price(laptop_data:LaptopData):
    # convert the data into dictionary
    data = {
        'Company':  laptop_data.Company,
        'TypeName':  laptop_data.TypeName,
        'Ram':  laptop_data.Ram,
        'Weight':  laptop_data.Weight,
        'Touchscreen': laptop_data.Touchscreen,
        'IPSpanel':  laptop_data.IPSpanel,
        'PPI': laptop_data.PPI,
        'RetinaDisplay':  laptop_data.RetinaDisplay,
        'CPU_freq':  laptop_data.CPU_freq,
        'CPU_brand':  laptop_data.CPU_brand,
        'Processor': laptop_data.Processor,
        'OS':  laptop_data.OS,
        'GPU_brand': laptop_data.GPU_brand,
        'PrimaryStorage': laptop_data.PrimaryStorage,
        'SecondaryStorage': laptop_data.SecondaryStorage,
        'PrimaryStorageType': laptop_data.PrimaryStorageType,
        'SecondaryStorageType': laptop_data.SecondaryStorageType
    }

    # convert the dictionary into dataframe df
    df = pd.DataFrame([data])

    # pass the data into the model
    predicted_price = int(np.exp(model.predict(df)[0]))

    # return the price
    return {
        'predicted_price': predicted_price
    }