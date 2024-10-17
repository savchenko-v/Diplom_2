class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    CREATE_USER = 'auth/register'
    LOGIN_USER = 'auth/login'
    INFO_USER = 'auth/user'
    ORDERS = 'orders'
    INGREDIENTS = 'ingredients'


class Responses:
    CREATE_SAME_USER = 'User already exists'
    CREATE_USER_WITHOUT_FIELD = 'Email, password and name are required fields'

    LOGIN_USER_INCORRECT_DATA = 'email or password are incorrect'

    USER_WITHOUT_AUTH = 'You should be authorised'

    ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'


class Ingredients:
    INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
