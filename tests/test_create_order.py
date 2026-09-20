import allure
import pytest

from data import ORDER_DATA_VARIANTS
from api.order_api import OrderApi


class TestCreateOrder:

    @allure.title('Успешное создание заказа с разными вариантами цвета')
    @pytest.mark.parametrize("payload", ORDER_DATA_VARIANTS)
    def test_create_order_with_different_colors_success(
            self, payload, order_cleanup):

        response = OrderApi.create_order(payload)

        order_cleanup.append(response.json()["track"])

        assert response.status_code == 201
        assert "track" in response.json()