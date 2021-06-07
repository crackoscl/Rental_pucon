
from django.urls import path
from .views import Principal, Reservar, Arrendar, Devolver, Ver_ficha
app_name = 'app'

urlpatterns = [
    path('', Principal.as_view(), name='principal'),
    path('reservar/<pk>', Reservar.as_view(), name='reservar'),
    path('arrendar/<pk>', Arrendar.as_view(), name='arrendar'),
    path('devolver/<pk>', Devolver.as_view(), name='devolver'),
    path('verficha/<pk>', Ver_ficha.as_view(), name='verficha'),
]
