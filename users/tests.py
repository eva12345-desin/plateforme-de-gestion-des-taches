from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthentificationTest(TestCase):
    def test_page_login_accessible(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_page_register_accessible(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_inscription_utilisateur(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'nouveluser',
            'password1': 'MotDePasseComplexe123',
            'password2': 'MotDePasseComplexe123',
        })
        self.assertEqual(User.objects.count(), 1)

    def test_connexion_utilisateur(self):
        User.objects.create_user(username='dave', password='testpass123')
        response = self.client.post(reverse('users:login'), {
            'username': 'dave',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)