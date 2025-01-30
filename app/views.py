from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class FilmesView(View):
    def get(self, request):
        filmes = Filme.objects.all()
        return render(request, 'filmes.html', {'filmes': filmes})

class SalasView(View):
    def get(self, request):
        salas = Sala.objects.all()
        return render(request, 'salas.html', {'salas': salas})

class SessoesView(View):
    def get(self, request):
        sessoes = Sessao.objects.select_related('filme', 'sala').all()
        return render(request, 'sessoes.html', {'sessoes': sessoes})

class IngressosView(View):
    def get(self, request):
        ingressos = Ingresso.objects.select_related('sessao').all()
        return render(request, 'ingresso.html', {'ingressos': ingressos})

class FuncionariosView(View):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        return render(request, 'funcionarios.html', {'funcionarios': funcionarios})
    
class SnacksView(View):
    def get(self, request):
        snacks = Snack.objects.all()
        return render(request, 'app/snacks.html', {'snacks': snacks})

        

class CidadesView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})
    


