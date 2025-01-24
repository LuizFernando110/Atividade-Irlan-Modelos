from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_modelos, name='listar_modelos'),
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhes_produto'),
    path('cadastro/', views.produtoFormView, name='cadastrar_produto'),
]
