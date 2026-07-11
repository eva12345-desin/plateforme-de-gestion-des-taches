from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.liste_projets, name='liste_projets'),
    path('creer/', views.creer_projet, name='creer_projet'),
    path('<int:projet_id>/', views.detail_projet, name='detail_projet'),
    path('<int:projet_id>/tache/creer/', views.creer_tache, name='creer_tache'),
]