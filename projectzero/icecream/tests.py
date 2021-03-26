from django.test import TestCase, Client
from django.urls import reverse
from .models import Ice_cream

class IcecreamTest(TestCase):
    def setUp(self):
        self.authorizate_client = Client()
    def test_correct_template(self):
        temp = {
            'icecream-detail.html':reverse('detail'),
            'icecream-list.html':reverse('icecream-list')
        }
        for k, v in temp.items():
            with self.subtest(k=k):
                form_field = self.authorizate_client.get(v)
                self.assertTemplateUsed(form_field, k)