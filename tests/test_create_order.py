from data import Urls, Responses, Ingredients
from helpers import TestDataHelper
import requests
import allure


class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth_ingredients(self, create_and_delete_user):
        data = create_and_delete_user
        register_response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)
        token = register_response.json()['accessToken']
        response = TestDataHelper.create_order(token, Ingredients.INGREDIENTS)

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Успешное создание заказа с ингредиентами и без авторизации')
    def test_create_order_with_ingredients_without_auth(self):
        response = TestDataHelper.create_order(token=None, ids=Ingredients.INGREDIENTS)

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка создания заказа без ингредиентов и без авторизации')
    def test_create_order_without_auth_ingredients(self):
        response = TestDataHelper.create_order(token=None, ids=None)

        assert response.status_code == 400 and response.json()['message'] == Responses.ORDER_WITHOUT_INGREDIENTS

    @allure.title('Проверка создания заказа с авторизацией и без ингредиентов')
    def test_create_order_with_auth_without_ingredients(self, create_and_delete_user):
        data = create_and_delete_user
        register_response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)
        token = register_response.json()['accessToken']
        response = TestDataHelper.create_order(token, ids=None)

        assert response.status_code == 400 and response.json()['message'] == Responses.ORDER_WITHOUT_INGREDIENTS

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_incorrect_hash(self):
        ingr_ids = [f'{Ingredients.INGREDIENTS[0]}1', Ingredients.INGREDIENTS[1]]
        response = TestDataHelper.create_order(token=None, ids=ingr_ids)

        assert response.status_code == 500
