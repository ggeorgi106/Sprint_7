import allure
import requests

from urls import CREATE_ORDER_URL, GET_ORDERS_URL, CANCEL_ORDER_URL


class OrderApi:

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(payload):
        return requests.post(CREATE_ORDER_URL, json=payload)

    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders():
        return requests.get(GET_ORDERS_URL)

    @staticmethod
    @allure.step('Отменить заказ')
    def cancel_order(track):
        return requests.put(CANCEL_ORDER_URL, json={"track": track})