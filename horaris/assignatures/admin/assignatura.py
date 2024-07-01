from django.contrib import admin
from django.utils.html import format_html
from datetime import datetime
from ..models.assignatura import Assignatura

@admin.register(Assignatura)
class AssignaturaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'hores_dedicacio', 'hores_setmanals', 'mostrar_resultats')

    def hores_setmanals(self, obj):
        return obj.hores_setmanals()
    hores_setmanals.short_description = 'Hores Setmanals'

    def mostrar_resultats(self, obj):
        data_inici = datetime(2023, 9, 1)  # Pots modificar aquesta data segons necessitis
        resultats_setmanes = obj.calcul_fi_resultats(data_inici)
        resultats_html = "<ul>"
        
        for resultat, data_inici, data_fi in resultats_setmanes:
            resultats_html += f"<li>{resultat.descripcio}: {data_inici.date()} - {data_fi.date()}</li>"
        
        resultats_html += "</ul>"
        return format_html(resultats_html)
    
    mostrar_resultats.short_description = 'Resultats i Setmanes'
