from django.contrib.auth import authenticate
from django.http import HttpRequest
from django.test import TestCase
from django.contrib.auth.models import User
from string import ascii_uppercase
from random import choice

from protection_mechanisms.settings import AXES_FAILURE_LIMIT


class LoginTestCase(TestCase):
    def setUp(self) -> None:
        self.credentials = {
            'username': 'username',
            'password': 'password'
        }
        User.objects.create_user(**self.credentials)

        self.simple_passwords = [
            {'username': 'admin', 'password': 'admin'},
            {'username': 'root', 'password': 'root'},
            {'username': 'denis', 'password': 'denis'},
        ]

    def test_active_debugger(self):
        self.assertFalse(DEBUG, msg='Включен деббагер')

    def test_empty_password(self):
        request = HttpRequest()
        user = authenticate(request, username=self.credentials['username'], password='')
        self.assertTrue(not user, msg='Удалось авторизоваться с пустым паролем')

    def test_empty_login(self):
        request = HttpRequest()
        user = authenticate(request, username='', password=self.credentials['username'])
        self.assertTrue(not user, msg='Удалось авторизоваться с пустым логином')

    def test_empty_login_and_password(self):
        request = HttpRequest()
        user = authenticate(request, username='', password='')
        self.assertTrue(not user, msg='Удалось авторизоваться с пустым логином и паролем')

    def test_brute_force(self):
        login_attempts_to_make = AXES_FAILURE_LIMIT + 4

        for i in range(login_attempts_to_make):
            password = ''.join([choice(ascii_uppercase) for j in range(6)])
            request = HttpRequest()
            authenticate(request, username=self.credentials['username'], password=password)

        # block to auth
        request = HttpRequest()
        user = authenticate(request, **self.credentials)
        self.assertFalse(user, 'AXES не заблокировал попытки входа')






