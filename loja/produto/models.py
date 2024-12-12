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
    
class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    produto = models.ManyToManyField(Produto)

    def __str__(self):
        return self.nome
    

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True, verbose_name='CNPJ')
    produto = models.ManyToManyField(Produto)

    class Meta:
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome