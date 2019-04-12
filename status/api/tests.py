# from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from status.models import Status


User = get_user_model()


class StatusAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='dev', email='pydev@ukr.net')
        user.set_password('1212qwqw')
        user.save()
        status_obj = Status.objects.create(user=user, content='Hello here!')

    def test_statuses(self):
        self.assertEqual(Status.objects.all().count(), 1)

    def status_user_token(self):
        auth_url = api_reverse('api-auth:login')
        auth_data = {
            'username': 'dev',
            'password': '1212qwqw',
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get('token', '')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def create_item(self):
        self.status_user_token()

        url = api_reverse('api-status:list')
        data = {'content': 'Some content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.all().count(), 2)
        return response.data

    def test_status_create(self):
        data = self.create_item()

        data_id = data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})

        # GET / retrieve
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_status_update(self):
        data = self.create_item()

        data_id = data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})
        rud_data = {'content': 'Another some content'}

        # PUT / update
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        rud_response_data = put_response.data
        self.assertEqual(rud_response_data['content'], rud_data['content'])

    def test_status_delete(self):
        data = self.create_item()

        data_id = data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})

        # DELETE / retrieve
        del_response = self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

        # not found
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_no_token_create(self):
        url = api_reverse('api-status:list')
        data = {'content': 'Some content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
