from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('nouvelleListe/', creer_liste, name='creer_liste'),
    path('liste/<int:id>', liste, name='liste'),
    path('liste/<int:id>/nouvelleTache', creer_tache, name='creer_tache'),
    path('liste/<int:id>/supprimer', supprimer_liste, name='supprimer_liste'),
    path('liste/<int:pk>/tache_details/<int:id>', tache_details_update, name='tache_details_update'),
    path('tache/<int:id>', supprimer_tache, name='supprimer_tache'),
]