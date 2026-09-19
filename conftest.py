import pytest

from helpers import generate_courier_data
from api.courier_api import CourierApi
from api.order_api import OrderApi


@pytest.fixture
def courier():
    payload = generate_courier_data()

    CourierApi.create_courier(payload)

    login_payload = {
        "login": payload["login"],
        "password": payload["password"]
    }

    login_response = CourierApi.login_courier(login_payload)
    courier_id = login_response.json()["id"]

    yield payload

    CourierApi.delete_courier(courier_id)


@pytest.fixture
def courier_cleanup():
    courier_ids = []

    yield courier_ids

    for courier_id in courier_ids:
        CourierApi.delete_courier(courier_id)


@pytest.fixture
def order_cleanup():
    order_tracks = []

    yield order_tracks

    for track in order_tracks:
        OrderApi.cancel_order(track)