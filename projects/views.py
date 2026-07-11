from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projet, Tache


@login_required
def liste_projets(request):
    projets = Projet.objects.filter(membres=request.user) | Projet.objects.filter(createur=request.user)
    projets = projets.distinct()
    return render(request, 'projects/liste_projets.html', {'projets': projets})


@login_required
def creer_projet(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        projet = Projet.objects.create(nom=nom, description=description, createur=request.user)
        projet.membres.add(request.user)
        return redirect('projects:detail_projet', projet_id=projet.id)
    return render(request, 'projects/creer_projet.html')


@login_required
def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()
    return render(request, 'projects/detail_projet.html', {'projet': projet, 'taches': taches})


@login_required
def creer_tache(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        Tache.objects.create(titre=titre, description=description, projet=projet)
        return redirect('projects:detail_projet', projet_id=projet.id)
    return render(request, 'projects/creer_tache.html', {'projet': projet})