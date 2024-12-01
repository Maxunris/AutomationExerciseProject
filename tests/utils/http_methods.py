import requests

class HttpMethods:
    headers = {'Content-type': 'application/x-www-form-urlencoded'}  # Передаем данные как x-www-form-urlencoded
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)  # Используем data
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)  # Используем data
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, data=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)  # Используем data
        return result
