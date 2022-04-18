<h1>Развернуть проект</h1>

1. Склонируйте проект 
2. Зайдите в корень проекта и настройте виртуальное окружение `python3 venv venv`, а после активируйте его `. venv\bin\activate`. Для Windows `venv\Scripts\activate.bat`
3. Установите библиотеки `pip install -r requirements.txt`
4. Накатите миграции `pyton manage.py migrate`
5. Создайте супер пользователя `python manage.py createsuperuser`, а потом от его имени создайте второй аккаунт и настройте на нем права доступа

<h1>AXES - ограничение попыток входа</h1>

```python
AXES_ENABLED = True  # Включить axes
AXES_USE_USER_AGENT = True # Записывать user-agent
AXES_COOLOFF_TIME = timedelta(seconds=10)  # Ограничение по времени
AXES_FAILURE_LIMIT = 3  # Количество неудачных попыток
AXES_LOCK_OUT_AT_FAILURE = True  # Блокировать IP после неудачной попытки входа
```


<h2>Запуск с ключом активации</h2>

`python manage autologin -u {username}`

После запуска приложения, пользователь всегда будет авторизован.

Если поле `username` оставить пустым, приложение будет работать как и при команде `runserver`.

<i>P.S.: Перед запуском убедитесь, что пользователь с таким юзернеймом существует</i>

<h2>Тесты</h2>

`python manage.py test conditional_сompilation.tests`
