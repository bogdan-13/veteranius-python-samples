from unittest import TestCase

import requests
from django.urls import reverse


class AlumiDBTestCase(TestCase):
    def setUp(self) -> None:
        self.site = 'http://127.0.0.1:8000'

    def test_login_get(self):
        url = reverse('login')
        response = requests.get(self.site+url)
        print(self.site+url, response)

    def test_logout_get(self):
        url = reverse('logout')
        response = requests.get(self.site + url)
        print(self.site + url, response)

    def test_register_get(self):
        url = reverse('register')
        response = requests.get(self.site+url)
        print(self.site+url, response)

    def test_user_get(self):
        url = reverse('viewuser')
        response = requests.get(self.site+url)
        print(self.site+url, response)

    def test_skill_get(self):
        url = reverse('viewskill')
        response = requests.get(self.site + url)
        print(self.site + url, response)

    def test_cert_get(self):
        url = reverse('viewcert')
        response = requests.get(self.site + url)
        print(self.site + url, response)

    def test_adduser_get(self):
        url = reverse('adduser')
        response = requests.get(self.site+url)
        print(self.site+url, response)

    def test_addskill_get(self):
        url = reverse('addskill')
        response = requests.get(self.site + url)
        print(self.site + url, response)

    def test_addcert_get(self):
        url = reverse('addcert')
        response = requests.get(self.site + url)
        print(self.site + url, response)

    def test_adminka_get(self):
        url = reverse('adminka')
        response = requests.get(self.site + url)
        print(self.site + url, response)