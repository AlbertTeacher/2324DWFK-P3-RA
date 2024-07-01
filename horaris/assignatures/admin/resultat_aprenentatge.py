from django.contrib import admin
from ..models.resultat_aprenentatge import ResultatAprenentatge

@admin.register(ResultatAprenentatge)
class ResultatAprenentatgeAdmin(admin.ModelAdmin):
    list_display = ('assignatura', 'descripcio', 'hores')
    list_filter = ('assignatura',)
