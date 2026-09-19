import requests
import pytest

from urls import LOGIN_COURIER_URL
from helpers import (
    register_new_courier_and_return_login_password,
    generate_random_string
)


class TestLoginCourier:

    def test_login_courier_success(self):
        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(LOGIN_COURIER_URL, data=payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_without_required_field_error(self, missing_field):
        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        payload.pop(missing_field)

        response = requests.post(LOGIN_COURIER_URL, data=payload)

        assert response.status_code == 400

    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_courier_with_wrong_credentials_error(self, wrong_field):
        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        payload[wrong_field] = generate_random_string(15)

        response = requests.post(LOGIN_COURIER_URL, data=payload)

        assert response.status_code == 404

    def test_login_nonexistent_courier_error(self):
        payload = {
            "login": generate_random_string(15),
            "password": generate_random_string(15)
        }

        response = requests.post(LOGIN_COURIER_URL, data=payload)

        assert response.status_code == 404