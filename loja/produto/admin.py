from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo_produto', 'nome', 'preco', 'quantidade_estoque', 'data_criacao')
    search_fields = ('codigo_produto', 'nome')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)

admin.site.register(Produto, ProdutoAdmin)
