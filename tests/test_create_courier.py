import allure
import pytest

from helpers import generate_courier_data
from api.courier_api import CourierApi


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, courier_cleanup):
        payload = generate_courier_data()

        response = CourierApi.create_courier(payload)

        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        login_response = CourierApi.login_courier(login_payload)
        courier_cleanup.append(login_response.json()["id"])

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Ошибка при создании двух одинаковых курьеров')
    def test_create_duplicate_courier_error(self, courier_cleanup):
        payload = generate_courier_data()

        CourierApi.create_courier(payload)
        response = CourierApi.create_courier(payload)

        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        login_response = CourierApi.login_courier(login_payload)
        courier_cleanup.append(login_response.json()["id"])

        assert response.status_code == 409

    @allure.title('Ошибка при создании курьера без обязательного поля')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_error(self, missing_field):
        payload = generate_courier_data()
        payload.pop(missing_field)

        response = CourierApi.create_courier(payload)

        assert response.status_code == 400