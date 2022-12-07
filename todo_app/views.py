from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):

    listes = TodoList.objects.all()

    dico = { "listes" : listes }

    return render(request, 'todo_app/index.html', dico)

def liste(request, id):

    liste = TodoList.objects.get(id=id)
    taches = TodoItem.objects.filter(liste=liste)

    dico = { "liste" : liste, "taches" : taches }

    return render(request, 'todo_app/liste.html', dico)

def creer_liste(request):

    if request.method == 'POST' :

        form = ListeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    else :

        form = ListeForm()

    dico = { "form" : form }

    return render(request, 'todo_app/creerListe.html', dico)

def creer_tache(request, id):

    liste = TodoList.objects.get(id=id)

    if request.method == 'POST' :

        form = TacheForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(f'/liste/{id}')

    else :

        form = TacheForm()

    dico = { "form" : form }

    return render(request, 'todo_app/creerTache.html', dico)

def tache_details_update(request, id, pk):

    task = TodoItem.objects.get(id=id)
    liste = TodoList.objects.get(id=pk)
    liste = liste.id

    if request.method == 'POST' :

        form = TacheForm(request.POST, instance=task)

        if form.is_valid() :

            form.save()

            return redirect(f'/liste/{liste}')
    
    else :

        form = TacheForm(instance=task)

    dico = { "form" : form, "tache" : task }

    return render(request, 'todo_app/tache.html', dico)

def supprimer_liste(request, id):

    liste = TodoList.objects.get(id=id)
    liste.delete()

    return redirect('/')

def supprimer_tache(request, id):

    tache = TodoItem.objects.get(id=id)
    liste = tache.liste
    liste_id = liste.id
    tache.delete()

    return redirect(f'/liste/{liste_id}')