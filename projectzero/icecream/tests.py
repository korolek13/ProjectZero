from django.test import TestCase, Client
from django.urls import reverse
from .models import Ice_cream, User
from django import forms

class IcecreamTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.task = Ice_cream.objects.create(
            name = 'Манговое',
            description = 'bla-bla',
            price = 1,
            rating = 0
        )
        cls.task = Ice_cream.objects.create(
            name = 'Манговое',
            description = 'bla-bla',
            price = 1,
            rating = 0
        )
        cls.task = Ice_cream.objects.create(
            name = 'Манговое',
            description = 'bla-bla',
            price = 1,
            rating = 0
        )
        cls.task = Ice_cream.objects.create(
            name = 'Манговое',
            description = 'bla-bla',
            price = 1,
            rating = 0
        )
        cls.user = User.objects.create(
            username='Testuser',
            password='1234567'
        )

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(IcecreamTest.user)

    def test_title_name(self):
        task = IcecreamTest.task
        verbose = task._meta.get_field("name").verbose_name
        self.assertEqual(verbose, 'имя')

    def test_homepage(self):
        response = self.guest_client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_icecream(self):
        response = self.guest_client.get("/icecream/")
        self.assertEqual(response.status_code, 200)

    def test_correct_template_for_icecream(self):
        response = self.guest_client.get("/icecream/")
        self.assertTemplateUsed(response, "icecream/icecream-list.html")

    def test_redirect_anonymus(self):
        response = self.guest_client.get("/icecream/1/")
        self.assertEqual(response.status_code, 302)

    def test_redirect_authorized(self): 
        response = self.authorized_client.get("/icecream/1/")
        self.assertEqual(response.status_code, 200)

    def test_correct_template_for_details(self):
        response = self.authorized_client.get(
            reverse('detail', kwargs={
                'pk':'1'
            }))
        self.assertTemplateUsed(response, 'icecream/icecream-detail.html')

    def test_correct_context_icecream(self):
        response = self.authorized_client.get(
            reverse('detail', kwargs={
                'pk':'1'
            })
        )
        self.assertIn('name', response.context)
        self.assertIn('avatar', response.context)
        self.assertIn('price', response.context)
        self.assertIn('description', response.context)
        self.assertIn('gold_rating', response.context)
        self.assertIn('gray_rating', response.context)

    def test_first_page(self):
        response = self.authorized_client.get(
            '/icecream/'
        )
        self.assertEqual(len(response.context.get('page').object_list), 3)
    
    def test_second_page(self):
        response = self.authorized_client.get(
            reverse('icecream-list')+'?page=2'
        )
        self.assertEqual(len(response.context.get('page').object_list), 1)