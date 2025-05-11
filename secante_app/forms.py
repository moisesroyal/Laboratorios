from django import forms

class SecanteForm(forms.Form):
    x0 = forms.FloatField(label='Valor de x0', required=True)
    x1 = forms.FloatField(label='Valor de x1', required=True)
    tol = forms.FloatField(label='Tolerancia', required=True)
    max_iter = forms.IntegerField(label='Máximo de Iteraciones', required=True)
