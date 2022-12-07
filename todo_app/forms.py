from django.forms import ModelForm
from .models import *

class ListeForm(ModelForm):

    class Meta:
        model = TodoList
        fields = ['titre']

class TacheForm(ModelForm):

    class Meta:
        model = TodoItem
        fields = ['titre', 'tache', 'statut', 'liste']