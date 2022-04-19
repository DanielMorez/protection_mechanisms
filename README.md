<h1>Развернуть проект</h1>

1. Склонируйте проект 
2. Зайдите в корень проекта и настройте виртуальное окружение `python3 venv venv`, а после активируйте его `. venv\bin\activate`
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

<h1>Запуск с ключом активации</h1>

`python manage autologin -u {username}`

После запуска приложения, пользователь всегда будет авторизован.

Если поле `username` оставить пустым, приложение будет работать как при команде `runserver`.

<i>P.S.: Перед запуском убедитесь, что пользователь с таким юзернеймом существует</i>

<h1>Тесты</h1>

`python manage.py test conditional_сompilation.tests`


<h1>Нагрузочное тестирование</h1>

<i>У вас должен быть установлен Docker</i>

1. В конфигурационном файле `load.yaml` установите порт, на котором работает ваше локальное приложение. 
Для Django порт по умолчанию `8000`.
   
2. Добавьте в корень проекта `token.txt`. Получить его можно на <a href='https://overload.yandex.net'>overload.yandex.net.</a>. 
Далее на этом сервисе вы сможете получить статистику по нагузке.

3. Запускаем танк из docker образа: `docker run -v {путь_до_проекта}:/var/loadtest --net host -it --entrypoint /bin/bash direvius/yandex-tank
`
   
4. Далее из под `[tank]root@docker-desktop` нужно выполнить  <a href='https://overload.yandex.net/mainpage/guide#install'>команды PIP-based installation</a>. 
   Иначе вы не сможете воспользоваться overload.yandex.net
   
5. Теперь вы готовы тестировать: `yandex-tank -c load.yaml`
