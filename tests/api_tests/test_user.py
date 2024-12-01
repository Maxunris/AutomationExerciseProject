from tests.utils.api import AutomationExerciseAPI
import allure


@allure.epic("Тесты с пользователем")
class TestUser:
    @allure.description("Создание, проверка на существование, проверка на описание, удаление пользователя")
    def test_create_user(self):
        with allure.step("Создание пользователя"):
            response = AutomationExerciseAPI.create_user()
            allure.attach(response.text, name="Ответ API", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Статус-код", attachment_type=allure.attachment_type.TEXT)
            assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
            assert "User created!" in response.text, f"Ожидали 'User created!', получили {response.text}"

    def test_verify_login(self):
        with allure.step("Проверка входа пользователя"):
            response = AutomationExerciseAPI.verify_login()
            allure.attach(response.text, name="Ответ API", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Статус-код", attachment_type=allure.attachment_type.TEXT)
            assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
            assert "User exists!" in response.text, f"Ожидали 'User exists!', получили {response.text}"

    def test_get_user_details(self):
        with allure.step("Получение деталей пользователя по email"):
            response = AutomationExerciseAPI.get_user_details_by_email()
            allure.attach(response.text, name="Ответ API", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Статус-код", attachment_type=allure.attachment_type.TEXT)
            assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
            assert "max245124512451@gmail.com" in response.text, f"Ожидали email, получили {response.text}"

    def test_delete_user(self):
        with allure.step("Удаление пользователя"):
            response = AutomationExerciseAPI.delete_user()
            allure.attach(response.text, name="Ответ API", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Статус-код", attachment_type=allure.attachment_type.TEXT)
            assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
            assert "Account deleted!" in response.text, f"Ожидали 'Account deleted!', получили {response.text}"

    def test_verify_login_after_delete(self):
        with allure.step("Проверка входа после удаления пользователя"):
            response = AutomationExerciseAPI.verify_login()
            allure.attach(response.text, name="Ответ API", attachment_type=allure.attachment_type.JSON)
            allure.attach(str(response.status_code), name="Статус-код", attachment_type=allure.attachment_type.TEXT)
            assert response.status_code == 200, f"Ожидался статус 200, получили {response.status_code}"
            assert "User not found!" in response.text, f"Ожидали 'User exists!', получили {response.text}"
            assert "404" in response.text, f"Ожидали 'User exists!', получили {response.text}"
