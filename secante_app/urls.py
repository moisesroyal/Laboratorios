# secante_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SecanteProblemaViewSet, add_problema, problema_list, problema_detail

router = DefaultRouter()
router.register(r'secante', SecanteProblemaViewSet, basename='secante')

urlpatterns = [
    path('api/', include(router.urls)),
    path('nuevo/', add_problema, name='formulario_secante'),
    path('problemas/', problema_list, name='problema_list'),
    path('problema/<int:pk>/', problema_detail, name='problema_detail'),
]
