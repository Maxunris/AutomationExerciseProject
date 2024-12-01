import json
import requests

def test_1():
    user_data = {
        "name": "Test User",
        "email": "max245124512451@gmail.com",
        "password": "password123",
        "title": "Mr",
        "birth_date": "1",
        "birth_month": "January",
        "birth_year": "1990",
        "firstname": "Test",
        "lastname": "User",
        "company": "TestCompany",
        "address1": "123 Test St",
        "address2": "Suite 456",
        "country": "United States",
        "zipcode": "12345",
        "state": "CA",
        "city": "Test City",
        "mobile_number": "1234567890"
    }

    url = "https://automationexercise.com/create_account"
    headers = {'Content-Type': 'application/json'}

    print("Request data:", json.dumps(user_data))

    response = requests.post(url, json=user_data, headers=headers)

    print(response.text)
    print(response.status_code)
