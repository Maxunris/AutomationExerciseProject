from tests.utils.api import AutomationExerciseAPI

class TestUser:
    def test_create_user(self):
        response = AutomationExerciseAPI.create_user()
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "User created!" in response.text, f"Ожидали 'User created!', получили {response.text}"

    def test_verify_login(self):
        response = AutomationExerciseAPI.verify_login()
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "User exists!" in response.text, f"Ожидали 'User exists!', получили {response.text}"

    def test_get_user_details(self):
        response = AutomationExerciseAPI.get_user_details_by_email()
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "max245124512451@gmail.com" in response.text, f"Ожидали email, получили {response.text}"

    def test_delete_user(self):
        response = AutomationExerciseAPI.delete_user()
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "Account deleted!" in response.text, f"Ожидали 'Account deleted!', получили {response.text}"

    def test_verify_login_after_delete(self):
        response = AutomationExerciseAPI.verify_login()
        assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
        assert "User not found!" in response.text, f"Ожидали 'User exists!', получили {response.text}"
        assert "404" in response.text, f"Ожидали 'User exists!', получили {response.text}"