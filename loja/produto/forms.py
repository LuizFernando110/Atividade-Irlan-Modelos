from django import forms
from .models import Produto, Fornecedor, Categoria
from django.core import validators
    

class produtoForm(forms.ModelForm):
    nome = forms.CharField(label="Nome", validators=[validators.MinLengthValidator(3)])
    codigo_produto = forms.CharField(label="Código do produto")
    descricao = forms.CharField(widget=forms.Textarea, label="Descrição")
    preco = forms.DecimalField(label="Preço", validators=[validators.MinValueValidator(0)])
    quantidade_estoque = forms.IntegerField(label="Quantidade em estoque", validators=[validators.MinValueValidator(0)])
    categoria = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), label="Categorias")
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all(), label="Fornecedor")

    def clean_codigo_produto(self):
        code = self.cleaned_data['codigo_produto']
        if not code.isalnum():
            raise forms.ValidationError("O código do produto deve conter apenas letras e números sem espaço.")
        return code


    class Meta:
        model = Produto
        fields = ['nome', 'codigo_produto', 'descricao', 'preco', 'quantidade_estoque', 'categoria', 'fornecedor']    