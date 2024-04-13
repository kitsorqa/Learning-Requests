import requests
from requests.auth import HTTPBasicAuth


#First_request
"""response = requests.get(
    url="https://petstore.swagger.io/v2/store/inventory",
    #auth=HTTPBasicAuth("username", "password"),
    headers={
        'api_key': "special-key"
    },
    #params={},
    #verify=False #ignoring ssl sertificate
)

print(response.json()['pending'])
print(response.status_code)"""

#Second_request
"""response = requests.get(
    url="https://petstore.swagger.io/v2/user/John",
    headers={
        'api_key': "special-key"
    }
)
print(response.json())"""

#Third_request
response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    headers={
        'api_key': "special-key"
    },
    params={
        "status": "pending"
    }
)
print(response.json())