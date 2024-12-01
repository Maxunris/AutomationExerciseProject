from tests.utils.http_methods import HttpMethods

class AutomationExerciseAPI:
    base_url = "https://automationexercise.com"
    test_email = "max245124512451@gmail.com"
    test_password = "password123"

    @staticmethod
    def search_product():
        """Метод для поиска продукта."""
        data = {
            "search_product": "Shirt"
        }
        url = f"{AutomationExerciseAPI.base_url}/api/searchProduct"
        print(url)
        result = HttpMethods.post(url, data)
        print(result.text)
        return result

    @staticmethod
    def create_user():
        """Метод для создания пользователя."""
        data = {
            "name": "Test User",
            "email": AutomationExerciseAPI.test_email,
            "password": AutomationExerciseAPI.test_password,
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
        url = f"{AutomationExerciseAPI.base_url}/api/createAccount"
        print(url)
        result = HttpMethods.post(url, data)
        print(result.text)
        return result

    @staticmethod
    def verify_login():
        """Метод для проверки входа пользователя."""
        data = {
            "email": AutomationExerciseAPI.test_email,
            "password": AutomationExerciseAPI.test_password
        }
        url = f"{AutomationExerciseAPI.base_url}/api/verifyLogin"
        print(url)
        result = HttpMethods.post(url, data)
        print(result.text)
        return result

    @staticmethod
    def delete_user():
        """Метод для удаления пользователя."""
        data = {
            "email": AutomationExerciseAPI.test_email,
            "password": AutomationExerciseAPI.test_password
        }
        url = f"{AutomationExerciseAPI.base_url}/api/deleteAccount"
        print(url)
        result = HttpMethods.delete(url, data)
        print(result.text)
        return result

    @staticmethod
    def get_user_details_by_email():
        """Метод для получения деталей пользователя по email."""
        params = {'email': AutomationExerciseAPI.test_email}
        url = f"{AutomationExerciseAPI.base_url}/api/getUserDetailByEmail"
        print(url)
        result = HttpMethods.get(url, params=params)
        print(result.text)
        return result
