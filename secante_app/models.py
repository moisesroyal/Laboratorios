# secante_app/models.py

from django.db import models

class SecanteProblema(models.Model):
    funcion = models.TextField()
    x0 = models.FloatField()
    x1 = models.FloatField()
    tolerancia = models.FloatField()
    max_iteraciones = models.IntegerField()
    resultado = models.FloatField(null=True, blank=True)
    iteraciones = models.IntegerField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.funcion} ({self.x0}, {self.x1})"
