import allure
import requests
import json

from tests.utils.logger import Logger

class HttpMethods:
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    cookie = ""

    @staticmethod
    def get(url, params=None):
        with allure.step("GET-запрос"):
            Logger.add_request(url, method="GET")
            allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
            if params:
                allure.attach(json.dumps(params, indent=4), name="Параметры запроса", attachment_type=allure.attachment_type.JSON)
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, params=params)
            Logger.add_response(result)
            allure.attach(result.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST-запрос"):
            Logger.add_request(url, method="POST")
            allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
            allure.attach(json.dumps(body, indent=4), name="Тело запроса", attachment_type=allure.attachment_type.JSON)
            result = requests.post(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            allure.attach(result.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT-запрос"):
            Logger.add_request(url, method="PUT")
            allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
            allure.attach(json.dumps(body, indent=4), name="Тело запроса", attachment_type=allure.attachment_type.JSON)
            result = requests.put(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            allure.attach(result.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE-запрос"):
            Logger.add_request(url, method="DELETE")
            allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
            allure.attach(json.dumps(body, indent=4), name="Тело запроса", attachment_type=allure.attachment_type.JSON)
            result = requests.delete(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            allure.attach(result.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
            return result
