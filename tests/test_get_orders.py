import requests

from urls import GET_ORDERS_URL


class TestGetOrders:

    def test_get_orders_returns_orders_list(self):
        response = requests.get(GET_ORDERS_URL)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)