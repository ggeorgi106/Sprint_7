import allure
import requests

from urls import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL


class CourierApi:

    @staticmethod
    @allure.step('Создать курьера')
    def create_courier(payload):
        return requests.post(CREATE_COURIER_URL, data=payload)

    @staticmethod
    @allure.step('Авторизовать курьера')
    def login_courier(payload):
        return requests.post(LOGIN_COURIER_URL, data=payload)

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(courier_id):
        return requests.delete(f'{DELETE_COURIER_URL}/{courier_id}')