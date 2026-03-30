import requests as rt
import smtplib,os
from dotenv import load_dotenv
# SHEETY_API = "https://api.sheety.co/8ee1390517e5fdb979232f99c3c6cea0/flightDeals/sheet1"
# SHEETY_HEADERS = {"Authorization": "Basic c3VtaXRoYTpzdW1pdGhhMTIz"}

class DataManager:
    def __init__(self):
        self.SHEETY_API = "https://api.sheety.co/8ee1390517e5fdb979232f99c3c6cea0/flightDeals/sheet1"
        self.SHEETY_HEADERS = {"Authorization": "Basic c3VtaXRoYTpzdW1pdGhhMTIz"}

    def get_data(self):
        flight_data = rt.get(url=self.SHEETY_API, headers=self.SHEETY_HEADERS)
        flight_data.raise_for_status()
        data = flight_data.json()["sheet1"]
        return data

    def update_data(self, object_id, data, to_update):
        new_data = {"sheet1": {f"{to_update}":data[f"{to_update}"]}}
        update_data = rt.put(url=f"{self.SHEETY_API}/{object_id}",headers=self.SHEETY_HEADERS, json=new_data)
        update_data.raise_for_status()
        print(update_data.text)








