from django.contrib import admin
from ..models.dia_de_festa import DiaDeFesta

@admin.register(DiaDeFesta)
class DiaDeFestaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'data')
    list_filter = ('data',)
