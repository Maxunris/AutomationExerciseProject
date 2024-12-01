from requests import Response
from tests.utils.api import AutomationExerciseAPI


class TestUser:
    def test_create_user(self):
        # Жестко заданный email для пользователя
        email = "max245124512451@gmail.com"

        # Данные для создания пользователя
        user_data = {
            "name": "Test User",  # Обязательный параметр
            "email": email,  # Жестко заданный email
            "password": "password123",  # Обязательный параметр
            "title": "Mr",  # Обязательный параметр
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

        # Создание пользователя
        response: Response = AutomationExerciseAPI.create_user(user_data)
        print(response.text)  # Логируем ответ для отладки
        print(response.status_code)  # Логируем ответ для отладки
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "User created!" in response.text, f"Ожидался ответ 'User created!' в ответе, получили {response.text}"
        assert "201" in response.text, f"Ожидался ответ 'User created!' в ответе, получили {response.text}"


    def test_delete_user(self):
        # Жестко заданный email для пользователя
        email = "max245124512451@gmail.com"

        # Данные для удаления пользователя
        delete_data = {
            "email": email,  # Жестко заданный email
            "password": "password123"  # Обязательный параметр
        }

        # Удаление пользователя
        response: Response = AutomationExerciseAPI.delete_user(delete_data)
        print(response.text)  # Логируем ответ для отладки
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "Account deleted!" in response.text, f"Ожидали 'Account deleted!' в ответе, получили {response.text}"
