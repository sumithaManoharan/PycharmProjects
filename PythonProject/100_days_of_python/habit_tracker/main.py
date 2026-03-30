import requests as rt
from datetime import datetime
TODAY_LOG = "5.00"
USERNAME = "sumitha"
TOKEN = "abcdefghijklmnopqrstuv"
DATE = datetime.today().strftime('%Y%m%d')

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = rt.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Ensure your endpoint ends at /graphs
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "coding_tracker",
    "unit": "hour",
    "type": "float",
    "color": "ichou"
}

headers = {"X-USER-TOKEN": TOKEN}

# response = rt.post(url=graph_endpoint, json=graph_config, headers=graph_headers)

graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
graph_data = {
    "date":DATE,
    "quantity":TODAY_LOG
}
response = rt.post(url = graph_value_endpoint, headers=headers, json=graph_data)
print(response.status_code)
print(DATE)