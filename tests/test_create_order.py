import requests
import pytest

from urls import CREATE_ORDER_URL
from data import ORDER_DATA, ORDER_COLORS


class TestCreateOrder:

    @pytest.mark.parametrize("color", ORDER_COLORS)
    def test_create_order_with_different_colors_success(self, color):
        payload = ORDER_DATA.copy()

        if color is not None:
            payload["color"] = color

        response = requests.post(CREATE_ORDER_URL, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()