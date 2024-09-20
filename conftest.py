from helpers import TestDataHelper
import pytest


@pytest.fixture()
def create_and_delete_user():  # создание данных для юзера для тестов и последующее удаление юзера
    user_data = TestDataHelper.create_user_data()

    yield user_data

    login_response = TestDataHelper.login_user(user_data)
    token = login_response.json()['accessToken']
    TestDataHelper.delete_user(token)
