import allure
import pytest

from helpers import generate_random_string
from api.courier_api import CourierApi


class TestLoginCourier:

    @allure.title('Успешный логин курьера')
    def test_login_courier_success(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }

        response = CourierApi.login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Ошибка логина курьера без обязательного поля')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_without_required_field_error(
            self, courier, missing_field):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        payload.pop(missing_field)

        response = CourierApi.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Ошибка логина курьера с неверными учётными данными')
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_courier_with_wrong_credentials_error(
            self, courier, wrong_field):
        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        payload[wrong_field] = generate_random_string(15)

        response = CourierApi.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Ошибка логина несуществующего курьера')
    def test_login_nonexistent_courier_error(self):
        payload = {
            "login": generate_random_string(15),
            "password": generate_random_string(15)
        }

        response = CourierApi.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"