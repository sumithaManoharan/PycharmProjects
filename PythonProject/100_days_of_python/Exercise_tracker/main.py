import requests as rt
import os
from datetime import datetime as dt
import pandas as pd

GENDER = "female"
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 24

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
GSHEET_KEY = "https://api.sheety.co/8ee1390517e5fdb979232f99c3c6cea0/myWorkouts/sheet1"

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = rt.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)
exercise_text = result["exercises"][0]
# print(exercise_text)
new_row = {
    "sheet1": {
        "date": dt.today().strftime("%d/%m/%Y"), # Using 2026
        "time": dt.now().strftime("%X"),          # Standard time format
        "exercise": exercise_text["name"].title(),
        "duration": exercise_text["duration_min"],
        "calories": exercise_text["nf_calories"]
    }
}
sheety_headers = {"Authorization": "Basic c3VtaXRoYTpzdW1pdGhhMTIz"}
add_row = rt.post(GSHEET_KEY, json=new_row, headers=sheety_headers)
print(add_row.text)
