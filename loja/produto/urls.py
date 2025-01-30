from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProdcutsListView.as_view(), name='products_list'),
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
    path('suppliers/', views.SuppliersListView.as_view(), name='suppliers_list'),
    path('produto/<int:pk>/', views.DetalhesProdutoView.as_view(), name='detalhes_produto'),
    path('cadastro/', views.CreateProductView.as_view(), name='cadastrar_produto'),
]
