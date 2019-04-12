from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='dev', email='pydev@ukr.net')
        user.set_password('1212qwqw')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='dev')
        self.assertEqual(qs.count(), 1)
