from data import Urls, Responses
from helpers import TestDataHelper
import requests
import allure


class TestLoginUser:

    @allure.title('Успешная авторизация пользователя')
    def test_login_user_success(self, create_and_delete_user):
        data = create_and_delete_user
        requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', json=data)  # создание пользователя
        response = TestDataHelper.login_user(data)  # логин пользователя

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Авторизация пользователя с неверным логином и паролем')
    def test_login_user_incorrect_data_error(self):
        data = TestDataHelper.create_user_data()
        response = TestDataHelper.login_user(data)

        assert response.status_code == 401 and response.json()['message'] == Responses.LOGIN_USER_INCORRECT_DATA
