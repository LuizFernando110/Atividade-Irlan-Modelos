from django import forms
from .models import Produto, Fornecedor, Categoria

class produtoForm(forms.Form):
    nome = forms.CharField(label="Nome")
    codigo_produto = forms.CharField(label="Código do produto")
    descricao = forms.CharField(widget=forms.Textarea, label="Descrição")
    preco = forms.DecimalField(label="Preço")
    quantidade_estoque = forms.IntegerField(label="Quantidade em estoque")
    categoria = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), label="Categorias")
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all(), label="Fornecedor")

    