from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seance(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    objet = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} à {self.heure_debut} avec {self.client.username}"
