from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produto, Fornecedor, Categoria
from .forms import produtoForm
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
class DetalhesProdutoView(DetailView):
    model = Produto
    template_name = 'detalhes_produto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto = self.get_object()
        context['produto'] = produto
        return context

class ProdcutsListView(ListView):
    model = Produto
    template_name = 'products_list.html'
    context_object_name =  'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ProdcutsListView, self).get_queryset()
        data = self.request.GET

        search = data.get('search')
        min_price = data.get('min_price')
        max_price = data.get('max_price')

        if search:
            queryset = queryset.filter(
                nome__icontains = search
            )
        
        if min_price:
            queryset = queryset.filter(
                preco__gte = min_price
            )
        
        if max_price:
            queryset = queryset.filter(
                preco__lte = max_price
            )

        return queryset

class SuppliersListView(ListView):
    model = Fornecedor
    template_name = 'suppliers_list.html'
    context_object_name =  'suppliers'

class CategoriesListView(ListView):
    model = Categoria
    template_name = 'categories_list.html'
    context_object_name =  'categories'


class CreateProductView(CreateView):
    model = Produto
    form_class = produtoForm
    template_name = 'produto_form.html'
    success_url = 'products_list'

