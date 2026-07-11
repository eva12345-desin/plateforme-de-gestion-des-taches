from django.db import models
from django.contrib.auth.models import User


class Projet(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    createur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projets_crees')
    membres = models.ManyToManyField(User, related_name='projets', blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Tache(models.Model):
    STATUT_CHOICES = [
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
    ]
    PRIORITE_CHOICES = [
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')
    assigne_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='taches_assignees')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='a_faire')
    priorite = models.CharField(max_length=20, choices=PRIORITE_CHOICES, default='moyenne')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titre