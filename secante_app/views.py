from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import SecanteProblema
from .serializers import SecanteProblemaSerializer
from .utils import metodo_secante, generar_grafica_convergencia

class SecanteProblemaViewSet(viewsets.ModelViewSet):
    queryset = SecanteProblema.objects.all().order_by('-creado_en')
    serializer_class = SecanteProblemaSerializer

def add_problema(request):
    if request.method == 'POST':
        funcion = request.POST['funcion']
        x0 = float(request.POST['x0'])
        x1 = float(request.POST['x1'])
        tolerancia = float(request.POST['tolerancia'])
        max_iteraciones = int(request.POST['max_iteraciones'])

        resultado, iteraciones, pasos = metodo_secante(funcion, x0, x1, tolerancia, max_iteraciones)
        pasos_redondeados = [round(p, 6) for p in pasos]

        if resultado is not None:
            problema = SecanteProblema.objects.create(
                funcion=funcion,
                x0=x0,
                x1=x1,
                tolerancia=tolerancia,
                max_iteraciones=max_iteraciones,
                resultado=resultado,
                iteraciones=iteraciones
            )

            grafica_base64 = generar_grafica_convergencia(pasos)

            return render(request, 'secante_app/resultados.html', {
                'resultado': problema,
                'pasos': pasos_redondeados,
                'grafica_base64': grafica_base64
            })
        else:
            return render(request, 'secante_app/resultados.html', {
                'error': 'Error al calcular la función. Revisa la sintaxis.',
            })

    return render(request, 'secante_app/add.html')

def problema_list(request):
    problemas = SecanteProblema.objects.all().order_by('-id')
    return render(request, 'secante_app/list.html', {'problemas': problemas})

def problema_detail(request, pk):
    problema = get_object_or_404(SecanteProblema, pk=pk)
    return render(request, 'secante_app/problema_detail.html', {'problema': problema})
