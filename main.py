import requests
from datetime import datetime

#user input parameters
USERNAME = 'CHOSEN USERNAME'
TOKEN = 'CHOSEN TOKEN'
graph_id = 'GRAPH_ID'

#URL endpoints
pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
value_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}'

#datetime module for date info
today = datetime.now().strftime('%Y%m%d')

#Parameters as JSON
pixela_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_config = {
    'id': graph_id,
    'name': 'TITLE OF GRAPH',
    'unit': 'Min',
    'type': 'int or float ',
    'color': 'ajisai'
}

value_config = {
    'date': today,
    'quantity': 'QUANT REQUIRED',
}

update_config = {
    'quantity': 'UPDATE QUANT'
}

#headers to pass token info
headers = {
    'X-USER-TOKEN': TOKEN
}

#create a new user
response = requests.post(url=pixela_endpoint, json=pixela_params)
print(response.text)

#create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#post value to graph
# response = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(response.text)

#update a specific pixel
# response = requests.put(url=f'{value_endpoint}/<yyyyMMdd>', json=update_config, headers=headers)
# print(response.text)

#delete a pixel
# response = requests.delete(url=f'{value_endpoint}/<yyyyMMdd>', headers=headers)
# print(response.text)

# #delete a graph
# response = requests.delete(url=value_endpoint, headers=headers)
# print(response.text)

#delete a user
# response = requests.delete(url=f'{pixela_endpoint}/{USERNAME}', headers=headers)
# print(response.text)
