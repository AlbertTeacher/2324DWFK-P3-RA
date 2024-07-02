from django.contrib import admin
from django.utils.html import format_html

from .resultat_aprenentatge import ResultatAprenentatgeInline
from ..models.assignatura import Assignatura

@admin.register(Assignatura)
class AssignaturaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'hores_dedicacio', 'data_inici', 'hores_setmanals', 'mostrar_resultats')
    list_editable = ('data_inici',)
    filter_horizontal = ('dies_de_festa',)
    inlines = [ResultatAprenentatgeInline]

    def hores_setmanals(self, obj):
        return obj.hores_setmanals()
    hores_setmanals.short_description = 'Hores Setmanals'

    def mostrar_resultats(self, obj):
        resultats_setmanes = obj.calcul_fi_resultats()
        resultats_html = "<ul>"
        
        for resultat, data_inici, data_fi in resultats_setmanes:
            resultats_html += f"<li>{resultat.descripcio}: {data_inici} - {data_fi}</li>"
        
        resultats_html += "</ul>"
        return format_html(resultats_html)
    
    mostrar_resultats.short_description = 'Resultats i Setmanes'
