from django.contrib import admin
from .models import Produto, Categoria, Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo_produto', 'nome', 'preco', 'quantidade_estoque', 'data_criacao')
    search_fields = ('codigo_produto', 'nome')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)

class categoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['produto']
    ordering = ['nome']


class fornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj']
    search_fields = ['nome', 'cnpj']
    list_filter = ['produto']
    ordering = ['nome']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, categoriaAdmin)
admin.site.register(Fornecedor, fornecedorAdmin)
