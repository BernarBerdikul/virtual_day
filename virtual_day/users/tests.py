from django.test import TestCase
from .models import User
from virtual_day.utils import constants


class UserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        password = "test_password"
        user = User.objects.create(
            email="test@mail.ru",
            role=constants.STUDENT,
            language=constants.SYSTEM_LANGUAGE,
            first_name="Test",
            last_name="Test",
            phone="+77074958782"
        )
        user.set_password(password)
        user.save()

    def test_get_user(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Почта')
