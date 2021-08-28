from unittest import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
import requests
from django.urls import reverse
from alumnidb.models import *
from alumnidb.utils import *


class AlumniDBAPITestCase(APITestCase):
    def test_skillview_set(self):
        skill_1 = Skills.objects.create(skill_name='test skill 1', skill_comments='test comment 1')
        skill_2 = Skills.objects.create(skill_name='test skill 2', skill_comments='test comment 2')
        url = reverse('skills-list')
        response = self.client.get(url)
        skills_data = SkillsView([skill_1, skill_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(skills_data, response.data)

    def test_userview_set(self):
        user_1 = Users.objects.create(ulastname_ua='test lastname 1', ufirstname_ua='test firstname 1',
                                      surname_ua='test surname 1', main_email='test email 1',
                                      user_comment='test comment 1')
        user_2 = Users.objects.create(ulastname_ua='test lastname 2', ufirstname_ua='test firstname 2',
                                      surname_ua='test surname 2', main_email='test email 2',
                                      user_comment='test comment 2')
        url = reverse('users-list')
        response = self.client.get(url)
        users_data = UsersView([user_1, user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(users_data, response.data)

    def test_certview_set(self):
        user_1 = Users.objects.create(ulastname_ua='test lastname 1', ufirstname_ua='test firstname 1',
                                      surname_ua='test surname 1', main_email='test email 1',
                                      user_comment='test comment 1')
        user_2 = Users.objects.create(ulastname_ua='test lastname 2', ufirstname_ua='test firstname 2',
                                      surname_ua='test surname 2', main_email='test email 2',
                                      user_comment='test comment 2')
        cert_1 = Certs.objects.create(user=user_1, data='2020-01-01', cert_number='1234567890')
        cert_2 = Certs.objects.create(user=user_2, data='2020-02-02', cert_number='0987654321')
        url = reverse('certs-list')
        response = self.client.get(url)
        certs_data = CertsView([cert_1, cert_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(certs_data, response.data)