from django.db import models

# Create your models here.
class TodoList(models.Model):

    titre = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class TodoItem(models.Model):

    titre = models.CharField(max_length=100)
    tache = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.BooleanField(default=False)
    liste = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre