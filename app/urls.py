from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('salas/', SalasView.as_view(), name='salas'),
    path('sessoes/', SessoesView.as_view(), name='sessoes'),
    path('ingresso/', IngressosView.as_view(), name='ingresso'),
    path('funcionarios/', FuncionariosView.as_view(), name='funcionarios'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('snaks/', SnaksView.as_view(), name='snaks'),
]
