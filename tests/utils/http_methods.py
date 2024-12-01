import allure
import requests

from tests.utils.logger import Logger


class HttpMethods:
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    cookie = ""

    @staticmethod
    def get(url, params=None):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, params=params)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result
