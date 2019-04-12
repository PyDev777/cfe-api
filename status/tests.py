from django.test import TestCase
from django.contrib.auth import get_user_model
from status.models import Status


User = get_user_model()


class StatusTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='dev', email='pydev@ukr.net')
        user.set_password('1212qwqw')
        user.save()

    def test_created_status(self):
        user = User.objects.get(username='dev')
        obj = Status.objects.create(user=user, content='Test content 1')
        self.assertEqual(obj.id, 1)

        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)
