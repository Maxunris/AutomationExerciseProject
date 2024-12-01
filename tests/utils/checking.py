import allure
import json

def check_status_code(result, status_code):
    """Метод для проверки статус кода"""
    with allure.step(f"Проверка статус-кода: ожидаемый {status_code}, полученный {result.status_code}"):
        assert status_code == result.status_code, f'ОШИБКА, Статус-код не совпадает. Ожидалось {status_code}, получено {result.status_code}'
        allure.attach(str(result.status_code), name="Статус-код", attachment_type=allure.attachment_type.TEXT)
        print(f"Успешно! Статус код = {result.status_code}")


def check_json_fields(result, expected_value):
    """Метод для проверки наличия полей в ответе запроса"""
    with allure.step("Проверка наличия полей в JSON-ответе"):
        fields = json.loads(result.text)
        allure.attach(json.dumps(fields, indent=4), name="JSON Ответ", attachment_type=allure.attachment_type.JSON)
        assert list(fields) == expected_value, f'ОШИБКА, Список полей не совпадает. Ожидали: {expected_value}, получили: {list(fields)}'
        allure.attach(str(expected_value), name="Ожидаемые поля", attachment_type=allure.attachment_type.TEXT)
        print(list(fields))
        print("Все поля присутствуют")


def check_json_value(result, field_name, expected_value):
    """Метод для проверки значений обязательных полей в ответе запроса"""
    with allure.step(f"Проверка значения поля {field_name}: ожидаемое {expected_value}"):
        check = result.json()
        check_info = check.get(field_name)
        allure.attach(json.dumps(check, indent=4), name="JSON Ответ", attachment_type=allure.attachment_type.JSON)
        assert check_info == expected_value, f'ОШИБКА, Значение поля не совпадает. Ожидалось: {expected_value}, получено: {check_info}'
        allure.attach(str(check_info), name=f"Полученное значение {field_name}", attachment_type=allure.attachment_type.TEXT)
        print(check_info)
        print(f"{field_name} верно!")
