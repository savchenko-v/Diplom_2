import requests
from faker import Faker
from data import Urls


class TestDataHelper:
    @staticmethod
    def create_user_data():
        fake = Faker()

        data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }

        return data

    @staticmethod
    def login_user(data):
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_USER}', json=data)

        return response

    @staticmethod
    def delete_user(token):
        response = requests.delete(f'{Urls.BASE_URL}{Urls.INFO_USER}', headers={'Authorization': token})

        return response

    @staticmethod
    def create_order(token, ids):
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS}', headers={'Authorization': token},
                                 data={'ingredients': ids})

        return response
