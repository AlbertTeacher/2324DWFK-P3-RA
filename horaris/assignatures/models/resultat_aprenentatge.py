from django.db import models
from .assignatura import Assignatura

class ResultatAprenentatge(models.Model):
    assignatura = models.ForeignKey(Assignatura, related_name='resultats_aprenentatge', on_delete=models.CASCADE)
    descripcio = models.TextField()
    hores = models.PositiveIntegerField()

    def __str__(self):
        return self.descripcio
