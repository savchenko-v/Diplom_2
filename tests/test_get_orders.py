from data import Urls, Responses
import requests
import allure


class TestGetOrders:
    @allure.title('Получение заказов конкретного пользователя - авторизованный пользователь')
    def test_get_orders_with_auth(self, create_and_delete_user):
        data = create_and_delete_user
        register_response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)
        token = register_response.json()['accessToken']
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS}', headers={'Authorization': token})

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Получение заказов конкретного пользователя - неавторизованный пользователь')
    def test_get_orders_without_auth(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS}')

        assert response.status_code == 401 and response.json()['message'] == Responses.USER_WITHOUT_AUTH
