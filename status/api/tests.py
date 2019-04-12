import os
import shutil
import tempfile
from PIL import Image
# from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from status.models import Status
from django.conf import settings

from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA



User = get_user_model()


class StatusAPITestCase(APITestCase):

    def setUp(self):
        self.test_user_name = 'testcfeuser'
        self.test_user_password = '111'
        self.test_user_email = 'pydev@ukr.net'

        # user = User.objects.create(username='dev', email='pydev@ukr.net')
        user = User.objects.create(username=self.test_user_name, email=self.test_user_email)
        user.set_password(self.test_user_password)
        user.save()
        status_obj = Status.objects.create(user=user, content='Hello here!')

    def test_statuses(self):
        self.assertEqual(Status.objects.all().count(), 1)

    def status_user_token(self):
        auth_url = api_reverse('api-auth:login')
        auth_data = {
            'username': self.test_user_name,
            'password': self.test_user_password,
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get('token', '')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def create_item(self):
        self.status_user_token()

        url = api_reverse('api-status:list')
        data = {
            'content': 'Some content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.all().count(), 2)
        return response.data

    def test_empty_create_item(self):
        self.status_user_token()

        url = api_reverse('api-status:list')
        data = {
            'content': None,
            'image': None,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Status.objects.all().count(), 1)

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
        rud_data = {
            'content': 'Another some content'
        }

        # PUT / update
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        rud_response_data = put_response.data
        self.assertEqual(rud_response_data['content'], rud_data['content'])

    def test_status_delete(self):
        data = self.create_item()

        data_id = data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})

        # DELETE / delete
        del_response = self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

        # Not found
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_no_token_create(self):
        url = api_reverse('api-status:list')
        data = {
            'content': 'Some content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_status_create_with_image(self):
        self.status_user_token()
        url = api_reverse('api-status:list')

        image_size = (640, 480)
        image_color = (0, 124, 174)
        image_item = Image.new('RGB', image_size, image_color)

        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')

        with open(tmp_file.name, 'rb') as file_obj:
            data = {
                'image': file_obj,
            }
            response = self.client.post(url, data, format='multipart')
            print(response.data)

            img_data = response.data.get('image')
            self.assertIsNotNone(img_data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Status.objects.all().count(), 2)

        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', self.test_user_name)
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)

    def test_status_create_with_image_and_desc(self):
        self.status_user_token()
        url = api_reverse('api-status:list')

        image_size = (640, 480)
        image_color = (0, 124, 174)
        image_item = Image.new('RGB', image_size, image_color)

        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')

        with open(tmp_file.name, 'rb') as file_obj:
            data = {
                'content': 'Content with image ' + str(image_size),
                'image': file_obj,
            }
            response = self.client.post(url, data, format='multipart')

            img_data = response.data.get('image')
            self.assertIsNotNone(img_data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Status.objects.all().count(), 2)

        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', self.test_user_name)
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)

    def test_other_user_permissions(self):
        data = self.create_item()
        data_id = data.get('id')
        user = User.objects.create(username='testjmitch')
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})
        rud_data = {
            'content': 'Other permissions'
        }
        get_ = self.client.get(rud_url, format='json')
        put_ = self.client.put(rud_url, rud_data, format='json')
        delete_ = self.client.delete(rud_url, format='json')
        self.assertEqual(get_.status_code, status.HTTP_200_OK)
        self.assertEqual(put_.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(delete_.status_code, status.HTTP_403_FORBIDDEN)
