from django.contrib import admin
from .models import *

class SessaoInline(admin.TabularInline):
    model = Sessao
    extra = 1

class IngressoInline(admin.TabularInline):
    model = Ingresso
    extra = 5

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'duracao', 'classificacao')
    search_fields = ('titulo', 'genero')
    inlines = [SessaoInline]

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade', 'tipo')
    search_fields = ('nome', 'tipo')
    inlines = [SessaoInline]

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'sala', 'horario', 'preco')
    list_filter = ('sala', 'horario')
    inlines = [IngressoInline]

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ('sessao', 'assento', 'vendido')
    list_filter = ('sessao', 'vendido')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'contato')
    search_fields = ('nome', 'cargo')
    

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Snaks)  
class SnaksAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'funcionario')  
    search_fields = ('nome', 'descricao')