from django.shortcuts import render
from django.views import View
from .models import Filme, Sessao

class IndexView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        return render(request, 'index.html', {'filmes': filmes})

class SessaoView(View):
    def get(self, request, *args, **kwargs):
        sessoes = Sessao.objects.all()
        return render(request, 'sessoes.html', {'sessoes': sessoes})
