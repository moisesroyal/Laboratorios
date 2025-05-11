from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Secante
from .serializers import SecanteSerializer
from .permissions import CanUseSecanteAPI  # O el permiso que hayas definido

class SecanteViewSet(viewsets.ModelViewSet):
    queryset = Secante.objects.all()
    serializer_class = SecanteSerializer
    permission_classes = [CanUseSecanteAPI]  # Define qué usuarios pueden usar este ViewSet
    
    @action(detail=True, methods=['POST'], url_path='resolver')
    def resolver(self, request, pk=None):
        secante = self.get_object()
        resultado = secante.resolver()  # Llama al método resolver() del modelo
        return Response({'resultado': resultado}, status=status.HTTP_200_OK)
