from django.test import Client, TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import response

from alumnidb.models import *
from alumnidb.views import *

User = get_user_model()


class AlumniDBTestCases(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        file = SimpleUploadedFile("new_file.pdf", content=b'', content_type="pdf")
        self.user = User.objects.create_user(username='testuser', email='test@test.ua', password='password')
        self.users = Users.objects.create(ulastname_ua='test lastname 1', ufirstname_ua='test firstname 1', surname_ua='test surname 1', main_email='test email 1', accaunt=self.user, user_comment='test comment 1')
        self.cert = Certs.objects.create(user=self.users, data='2020-01-01', cert_number='1234567890', cert_file=file)
        self.skill = Skills.objects.create(skill_name='test skill 1', skill_comments='test comment 1')

    def test_login_resp(self):
        client = Client()
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)

    def test_users_resp(self):
        client = Client()
        self.client.post(reverse('adduser'), {'ulastname_ua': 'test lastname 2', 'ufirstname_ua': 'test firstname 2', 'surname_ua': 'test surname 2', 'main_email': 'main@email.com', 'user_comment': 'test comment 2'})
        response = client.get('/user/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['view']), 2)

    def test_skill_resp(self):
        client = Client()
        data = {'skill_name': 'test skill 2', 'skill_comments': 'test comment 2'}
        self.client.post(reverse('addskill'), data)
        response = client.get('/skill/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['view']), 2)
        test_skill = Skills.objects.get(skill_name='test skill 2')
        self.assertEqual(test_skill.skill_comments, data['skill_comments'])

    def test_cert_resp(self):
        client = Client()
        response = client.get('/cert/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['view']), 1)
        print(response.context['view'])
        client.get('/cert/'+str(response.context['view'].first().id)+'/del')
        response2 = client.get('/cert/')
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(len(response2.context['view']), 1)

    def test_certsearch_resp(self):
        client = Client()
        response = self.client.get(reverse('homepage'), {'s': '1234567890'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['certsearch'].first(), self.cert)
