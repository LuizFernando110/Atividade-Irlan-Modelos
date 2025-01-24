from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produto, Fornecedor, Categoria
from .forms import produtoForm


# Create your views here.
def detalhe_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def listar_modelos(request):
    fornecedores = Fornecedor.objects.all()
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'listar_modelos.html', {'fornecedores': fornecedores, 'categorias': categorias, 'produtos': produtos})

def produtoFormView(request):
    if request.method == 'POST':
        form = produtoForm(request.POST)
        if form.is_valid():
            # Cria a instância sem salvar o campo ManyToManyField
            produto = Produto.objects.create(
                nome=form.cleaned_data['nome'],
                codigo_produto=form.cleaned_data['codigo_produto'],
                descricao=form.cleaned_data['descricao'],
                preco=form.cleaned_data['preco'],
                quantidade_estoque=form.cleaned_data['quantidade_estoque'],
                fornecedor=form.cleaned_data['fornecedor']
            )
            
            # Configura o campo ManyToManyField usando o método `set`
            produto.categoria.set(form.cleaned_data['categoria'])
            
            # Redireciona após salvar
            return HttpResponseRedirect(reverse('listar_modelos'))
        else:
            # Se o formulário não for válido, renderiza novamente com erros
            return render(request, 'produto_form.html', {'form': form})

    # Requisição GET: exibe o formulário vazio
    form = produtoForm()
    return render(request, 'produto_form.html', {'form': form})
