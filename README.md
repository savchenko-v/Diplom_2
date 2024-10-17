## Дипломный проект. Задание 2: API

### Тесты ручек API для [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
[Документация](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89) для сервиса.

### Реализованные сценарии:
- Создание пользователя
- Логин пользователя
- Изменение данных пользователя
- Создание заказа
- Получение заказов конкретного пользователя

#### Установить зависимости:

> pip install -r requirements.txt

#### Запустить все тесты:

> pytest -v

#### Посмотреть отчёт в браузере:

> allure serve allure_results
>
#### Создать новый отчёт:

> pytest tests --alluredir=allure_results
