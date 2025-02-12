from django.db import models
from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()  
    classificacao = models.CharField(max_length=20)
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo

class Sala(models.Model):
    nome = models.CharField(max_length=50)
    capacidade = models.PositiveIntegerField()
    tipo = models.CharField(max_length=50)  

    def __str__(self):
        return self.nome

class Sessao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'


    def __str__(self):
        return f"{self.filme} - {self.horario}"

class Ingresso(models.Model):
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    assento = models.CharField(max_length=10)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return f"Assento: {self.assento} - Sessão: {self.sessao.filme.titulo} às {self.sessao.horario.strftime('%H:%M')}"


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=100, unique=True, default='--')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
     
class Snaks(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    funcionario = models.ForeignKey(Funcionario, related_name='snaks', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Snak'
        verbose_name_plural = 'Snaks'