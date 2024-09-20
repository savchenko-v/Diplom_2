from data import Urls, Responses
from helpers import TestDataHelper
import requests
import pytest
import allure


class TestUpdateUser:

    @allure.title('Успешное изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize('update_field', ['email', 'password', 'name'])
    def test_update_user_success(self, create_and_delete_user, update_field):
        data = create_and_delete_user
        register_response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)  # создание пользователя
        token = register_response.json()['accessToken']  # получение токена
        data[update_field] += '1'  # изменение данных
        response = requests.patch(f'{Urls.BASE_URL}{Urls.INFO_USER}', json=data, headers={'Authorization': token})

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка изменения данных пользователя без авторизации')
    @pytest.mark.parametrize('update_field', ['email', 'password', 'name'])
    def test_update_user_without_auth_error(self, update_field):
        data = TestDataHelper.create_user_data()
        requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)
        data[update_field] += '1'
        response = requests.patch(f'{Urls.BASE_URL}{Urls.INFO_USER}', json=data)

        assert response.status_code == 401 and response.json()['message'] == Responses.USER_WITHOUT_AUTH
