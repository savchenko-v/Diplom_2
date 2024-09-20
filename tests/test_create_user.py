from data import Urls, Responses
from helpers import TestDataHelper
import requests
import pytest
import allure


class TestCreateUser:

    @allure.title('Успешное создание уникального пользователя')
    def test_create_user_success(self, create_and_delete_user):
        data = create_and_delete_user
        response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    def test_create_same_user_error(self):
        data = TestDataHelper.create_user_data()
        requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)
        response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)

        assert response.status_code == 403 and response.json()['message'] == Responses.CREATE_SAME_USER

    @allure.title('Создание пользователя с незаполненным обязательным полем')
    @pytest.mark.parametrize('delete_field', ['email', 'password', 'name'])
    def test_create_user_without_required_field_error(self, delete_field):
        data = TestDataHelper.create_user_data()
        del data[delete_field]
        response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)

        assert response.status_code == 403 and response.json()['message'] == Responses.CREATE_USER_WITHOUT_FIELD
