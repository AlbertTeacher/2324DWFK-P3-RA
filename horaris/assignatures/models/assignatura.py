from datetime import timedelta

from django.db import models


SATURDAY = 5
DAYS_PER_WEEK = 7
COURSE_WEEKS = 33
WORKDAYS = 5

class Assignatura(models.Model):
    nom = models.CharField(max_length=100)
    hores_dedicacio = models.PositiveIntegerField()
    data_inici = models.DateField()

    def __str__(self):
        return self.nom

    def troba_dilluns(self, data):
        dies_a_dilluns = (DAYS_PER_WEEK - data.weekday()) % DAYS_PER_WEEK
        return data + timedelta(days=dies_a_dilluns)

    def hores_setmanals(self):
        return self.hores_dedicacio / COURSE_WEEKS

    def calcul_fi_resultats(self):
        def add_weekdays(start_date, days):
            current_date = start_date
            while days > 0:
                current_date += timedelta(days=1)
                if current_date.weekday() < SATURDAY:
                    days -= 1
            return current_date

        resultats = self.resultats_aprenentatge.all()
        data_actual = self.data_inici
        resultats_setmanes = []
        
        for resultat in resultats:
            setmanes = resultat.hores / self.hores_setmanals()
            dies = int(setmanes * 5)
            data_fi = add_weekdays(data_actual, dies)
            resultats_setmanes.append((resultat, self.troba_dilluns(data_actual), self.troba_dilluns(data_fi)))
            data_actual = data_fi

        return resultats_setmanes