# secante_app/serializers.py

from rest_framework import serializers
from .models import SecanteProblema
import math

class SecanteProblemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecanteProblema
        fields = '__all__'
        read_only_fields = ['resultado', 'iteraciones']

    def create(self, validated_data):
        funcion_str = validated_data['funcion']
        x0 = validated_data['x0']
        x1 = validated_data['x1']
        tolerancia = validated_data['tolerancia']
        max_iter = validated_data['max_iteraciones']

        def f(x):
            try:
                return eval(funcion_str, {"x": x, "math": math, "__builtins__": {}})
            except Exception:
                raise serializers.ValidationError("Error evaluando la función.")

        for i in range(max_iter):
            try:
                fx0 = f(x0)
                fx1 = f(x1)
                if fx1 - fx0 == 0:
                    break
                x2 = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
                if abs(x2 - x1) < tolerancia:
                    validated_data['resultado'] = x2
                    validated_data['iteraciones'] = i + 1
                    break
                x0, x1 = x1, x2
            except Exception:
                raise serializers.ValidationError("Error durante el cálculo.")

        else:
            validated_data['resultado'] = x1
            validated_data['iteraciones'] = max_iter

        return super().create(validated_data)
