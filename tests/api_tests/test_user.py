from requests import Response
from tests.utils.api import AutomationExerciseAPI


class TestUser:
    def test_create_user(self):
        email = "max245124512451@gmail.com"

        user_data = {
            "name": "Test User",
            "email": email,
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

        response = AutomationExerciseAPI.create_user(user_data)
        print(response.text)
        print(response.status_code)
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "User created!" in response.text, f"Ожидался ответ 'User created!' в ответе, получили {response.text}"
        assert "201" in response.text, f"Ожидался ответ 'User created!' в ответе, получили {response.text}"

    def test_verify_login(self):
        email = "max245124512451@gmail.com"

        login_data = {
            "email": email,
            "password": "password123"
        }

        response = AutomationExerciseAPI.verify_login(login_data)
        print(response.text)
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "User exists!" in response.text, f"Ожидали 'User exists!' в ответе, получили {response.text}"
        assert "200" in response.text, f"Ожидали 'User exists!' в ответе, получили {response.text}"

    def test_get_user_details(self):
        email = "max245124512451@gmail.com"

        response = AutomationExerciseAPI.get_user_details_by_email(email)
        print(response.text)

        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"

        assert email in response.text, f"Ожидали email '{email}' в ответе, получили {response.text}"

        assert '"name": "Test User"' in response.text, f"Ожидалось имя пользователя, получили {response.text}"
        assert '"title": "Mr"' in response.text, f"Ожидалось звание 'Mr', получили {response.text}"
        assert '"birth_day": "1"' in response.text, f"Ожидалась дата рождения '1', получили {response.text}"
        assert '"birth_month": "January"' in response.text, f"Ожидался месяц рождения 'January', получили {response.text}"
        assert '"birth_year": "1990"' in response.text, f"Ожидался год рождения '1990', получили {response.text}"
        assert '"first_name": "Test"' in response.text, f"Ожидалось имя 'Test', получили {response.text}"
        assert '"last_name": "User"' in response.text, f"Ожидалась фамилия 'User', получили {response.text}"
        assert '"company": "TestCompany"' in response.text, f"Ожидалась компания 'TestCompany', получили {response.text}"
        assert '"address1": "123 Test St"' in response.text, f"Ожидался адрес '123 Test St', получили {response.text}"
        assert '"address2": "Suite 456"' in response.text, f"Ожидался адрес 'Suite 456', получили {response.text}"
        assert '"country": "United States"' in response.text, f"Ожидалась страна 'United States', получили {response.text}"
        assert '"state": "CA"' in response.text, f"Ожидалось состояние 'CA', получили {response.text}"
        assert '"city": "Test City"' in response.text, f"Ожидался город 'Test City', получили {response.text}"
        assert '"zipcode": "12345"' in response.text, f"Ожидался индекс '12345', получили {response.text}"


    def test_delete_user(self):
        email = "max245124512451@gmail.com"

        delete_data = {
            "email": email,
            "password": "password123"
        }
        response = AutomationExerciseAPI.delete_user(delete_data)
        print(response.text)
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "Account deleted!" in response.text, f"Ожидали 'Account deleted!' в ответе, получили {response.text}"
