import requests
from datetime import datetime
import os

gender = "male"
weight_kg = 65
height_cm = 175
age = 20

application_id = os.environ.get("API_ID")
application_key = os.environ.get("API_KEY")

end_point_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("Tell me which exercises you did: ")

header = {
    "x-app-id": application_id,
    "x-app-key": application_key
}

params = {
    "query": query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age,
}
response = requests.post(url=end_point_exercise, headers=header, json=params)
result = response.json()
print(result)


date = datetime.now()
date_now = date.strftime("%d-%m-%Y")
time = date.strftime("%H:%M")

sheety_url = os.environ.get("SHEETY_URL")
token = os.environ.get("SHEETY_TOKEN")
headers = {"Authorization": token}

for item in result["exercises"]:
    sheety_params = {
        "list1": {
            "date": date_now,
            "time": time,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        }
    }
    sheet_response = requests.post(sheety_url, json=sheety_params, headers=headers)
    print(sheet_response.json())
