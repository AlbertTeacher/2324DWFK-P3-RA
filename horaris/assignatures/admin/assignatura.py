from django.contrib import admin
from ..models.assignatura import Assignatura

@admin.register(Assignatura)
class AssignaturaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'hores_dedicacio')
