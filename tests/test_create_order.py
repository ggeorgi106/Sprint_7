import allure
import pytest

from data import ORDER_DATA, ORDER_COLORS
from api.order_api import OrderApi


class TestCreateOrder:

    @allure.title('Успешное создание заказа с разными вариантами цвета')
    @pytest.mark.parametrize("color", ORDER_COLORS)
    def test_create_order_with_different_colors_success(
            self, color, order_cleanup):
        payload = ORDER_DATA.copy()

        if color is not None:
            payload["color"] = color

        response = OrderApi.create_order(payload)

        order_cleanup.append(response.json()["track"])

        assert response.status_code == 201
        assert "track" in response.json()