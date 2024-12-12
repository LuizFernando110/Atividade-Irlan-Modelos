from django.shortcuts import render
from .models import Produto, Fornecedor, Categoria

# Create your views here.
def detalhe_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def listar_modelos(request):
    fornecedores = Fornecedor.objects.all()
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'listar_modelos.html', {'fornecedores': fornecedores, 'categorias': categorias, 'produtos': produtos})
