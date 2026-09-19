import requests
import pytest

from urls import CREATE_COURIER_URL
from helpers import generate_courier_data


class TestCreateCourier:

    def test_create_courier_success(self):
        payload = generate_courier_data()

        response = requests.post(CREATE_COURIER_URL, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier_error(self):
        payload = generate_courier_data()

        requests.post(CREATE_COURIER_URL, data=payload)
        response = requests.post(CREATE_COURIER_URL, data=payload)

        assert response.status_code == 409

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_error(self, missing_field):
        payload = generate_courier_data()
        payload.pop(missing_field)

        response = requests.post(CREATE_COURIER_URL, data=payload)

        assert response.status_code == 400