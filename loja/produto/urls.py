from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_modelos, name='lista_modelos'),
    path('produto/<produto_id>/', views.detalhe_produto, name='detalhes_produto'),
]
