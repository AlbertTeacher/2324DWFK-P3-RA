from django.contrib import admin
from ..models.resultat_aprenentatge import ResultatAprenentatge

class ResultatAprenentatgeInline(admin.TabularInline):
    model = ResultatAprenentatge
    extra = 0
