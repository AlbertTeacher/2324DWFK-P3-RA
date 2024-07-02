from django.db import models

class DiaDeFesta(models.Model):
    nom = models.CharField(max_length=100)
    data = models.DateField()

    def __str__(self):
        return f'{self.nom} ({self.data})'
