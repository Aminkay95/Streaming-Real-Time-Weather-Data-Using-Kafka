import requests
import json
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd


# variables  

load_dotenv()
uri = os.getenv('DB_STRING')

# Create a new client and connect to the server

client = MongoClient(uri, server_api=ServerApi('1'))
weather_api_key = os.getenv('WEATHER_API_KEY')

# Assigning variables 
city_name = 'Nairobi'

weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}'

def extract_data():
    response = requests.get(weather_url)

    data = response.json()
    weather_df = pd.DataFrame(data['weather'],index=[1])
    temp_df = pd.DataFrame(data['main'],index=[1])

    country = data['sys']['country']
    location_df = pd.DataFrame(
        {'country':country,
        'city': city_name }, index=[1]
    )

    merged_df = pd.merge(pd.merge(location_df,weather_df, how='outer', left_index=True, right_index=True), temp_df, how='outer', left_index=True, right_index=True)

    return merged_df

def transform_data(merged_df):
    
    #dropping columns id, icon since we dont need them
    merged_df = merged_df.drop(columns=['id','icon'])
    
    #transforing temp values from Kelvin to celcius
    cols_adjusted = ['temp', 'feels_like','temp_min','temp_max']
    merged_df[cols_adjusted] = merged_df[cols_adjusted] - 273
    data_dict = merged_df.to_dict(orient='records')

    return data_dict

def load_data_to_db(data_dict):

    db = client['weather_db']

    collection = db['weather_data']
    collection.insert_many(data_dict)






