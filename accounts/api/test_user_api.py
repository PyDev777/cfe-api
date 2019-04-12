# from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status


User = get_user_model()


class UserAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='dev', email='pydev@ukr.net')
        user.set_password('1212qwqw')
        user.save()

    def test_create_user(self):
        qs = User.objects.filter(username='dev')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'reg',
            'email': 'pydev-reg@ukr.net',
            'password': '1212qwqw',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password2'][0], 'This field is required.')

    def test_register_user_api(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'reg',
            'email': 'pydev-reg@ukr.net',
            'password': '1212qwqw',
            'password2': '1212qwqw',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token = response.data.get('token', '')
        self.assertGreater(len(token), 0)

    def test_login_user_api_fail(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'reg',
            'password': '1212qwqw',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        token = response.data.get('token', '')
        self.assertEqual(len(token), 0)

    def test_login_user_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'dev',
            'password': '1212qwqw',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', '')
        self.assertGreater(len(token), 0)

    def test_token_login_user_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'dev',
            'password': '1212qwqw',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', '')
        self.assertGreater(len(token), 0)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

    def test_token_register_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'dev',
            'password': '1212qwqw',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', '')
        self.assertGreater(len(token), 0)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        url2 = api_reverse('api-auth:register')
        data2 = {
            'username': 'reg',
            'email': 'pydev-reg@ukr.net',
            'password': '1212qwqw',
            'password2': '1212qwqw',
        }
        response = self.client.post(url2, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
