from datetime import timedelta

from django.db import models


class Assignatura(models.Model):
    nom = models.CharField(max_length=100)
    hores_dedicacio = models.PositiveIntegerField()

    def __str__(self):
        return self.nom

    def hores_setmanals(self):
        return self.hores_dedicacio / 33

    def calcul_fi_resultats(self, data_inici):
        resultats = self.resultats_aprenentatge.all()
        data_actual = data_inici
        resultats_setmanes = []
        
        for resultat in resultats:
            setmanes = resultat.hores / self.hores_setmanals()
            data_fi = data_actual + timedelta(weeks=setmanes)
            resultats_setmanes.append((resultat, data_actual, data_fi))
            data_actual = data_fi

        return resultats_setmanes