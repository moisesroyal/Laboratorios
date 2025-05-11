# secante_app/admin.py
from django.contrib import admin
from .models import SecanteProblema

@admin.register(SecanteProblema)
class SecanteProblemaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'funcion', 'x0', 'x1', 'tolerancia',
        'max_iteraciones', 'resultado', 'iteraciones', 'creado_en'
    )
    search_fields = ('funcion',)
    list_filter = ('creado_en',)
