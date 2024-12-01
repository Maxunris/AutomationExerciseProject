from tests.utils.http_methods import HttpMethods

base_url = "https://automationexercise.com"

class AutomationExerciseAPI:

    @staticmethod
    def search_product(search_query):
        data_for_search_product = {
            "search_product": search_query
        }
        post_resource_search_product = "/api/searchProduct"
        post_url_search_product = base_url + post_resource_search_product
        print(post_url_search_product)
        result_post = HttpMethods.post(post_url_search_product, data_for_search_product)
        print(result_post.text)
        return result_post

    @staticmethod
    def create_user(data):
        post_resource_create_user = "/api/createAccount"
        post_url_create_user = base_url + post_resource_create_user
        print(post_url_create_user)
        result_post = HttpMethods.post(post_url_create_user, data)
        print(result_post.text)
        return result_post

    @staticmethod
    def verify_login(data):
        post_resource_verify_login = "/api/verifyLogin"
        post_url_verify_login = base_url + post_resource_verify_login
        print(post_url_verify_login)
        result_post = HttpMethods.post(post_url_verify_login, data)
        print(result_post.text)
        return result_post

    @staticmethod
    def delete_user(data):
        delete_resource_delete_user = "/api/deleteAccount"
        delete_url_delete_user = base_url + delete_resource_delete_user
        print(delete_url_delete_user)
        result_delete = HttpMethods.delete(delete_url_delete_user, data)
        print(result_delete.text)
        return result_delete
