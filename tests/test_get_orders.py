import allure

from api.order_api import OrderApi


class TestGetOrders:

    @allure.title('Получение списка заказов')
    def test_get_orders_returns_orders_list(self):
        response = OrderApi.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)