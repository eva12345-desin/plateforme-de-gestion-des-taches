from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Projet, Tache


class ProjetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='testpass123')

    def test_creation_projet(self):
        projet = Projet.objects.create(nom='Projet Test', createur=self.user)
        self.assertEqual(projet.nom, 'Projet Test')
        self.assertEqual(projet.createur, self.user)

    def test_str_projet(self):
        projet = Projet.objects.create(nom='Mon Projet', createur=self.user)
        self.assertEqual(str(projet), 'Mon Projet')


class TacheModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='testpass123')
        self.projet = Projet.objects.create(nom='Projet Test', createur=self.user)

    def test_creation_tache(self):
        tache = Tache.objects.create(titre='Ma tâche', projet=self.projet)
        self.assertEqual(tache.statut, 'a_faire')
        self.assertEqual(tache.priorite, 'moyenne')

    def test_tache_liee_au_projet(self):
        Tache.objects.create(titre='Tâche 1', projet=self.projet)
        Tache.objects.create(titre='Tâche 2', projet=self.projet)
        self.assertEqual(self.projet.taches.count(), 2)


class VuesProjetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='carla', password='testpass123')
        self.client.login(username='carla', password='testpass123')

    def test_liste_projets_accessible(self):
        response = self.client.get(reverse('projects:liste_projets'))
        self.assertEqual(response.status_code, 200)

    def test_creer_projet(self):
        response = self.client.post(reverse('projects:creer_projet'), {
            'nom': 'Nouveau Projet',
            'description': 'Une description'
        })
        self.assertEqual(Projet.objects.count(), 1)
        self.assertEqual(response.status_code, 302)

    def test_acces_refuse_sans_connexion(self):
        self.client.logout()
        response = self.client.get(reverse('projects:liste_projets'))
        self.assertEqual(response.status_code, 302)