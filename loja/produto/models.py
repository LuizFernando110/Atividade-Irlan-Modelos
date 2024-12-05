from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo_produto = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2) 
    quantidade_estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome