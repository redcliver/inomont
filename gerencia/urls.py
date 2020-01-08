from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^colaboradores/', views.colaboradores),
    url(r'^colaboradoresNovo/', views.colaboradoresNovo),
    url(r'^colaboradoresVisualizar/', views.colaboradoresVisualizar),
    url(r'^colaboradoresSite/', views.colaboradoresSite),
    url(r'^colaboradoresSiteVisualizar/', views.colaboradoresSiteVisualizar),
    url(r'^fornecedores/', views.fornecedores),
    url(r'^fornecedoresNovo/', views.fornecedoresNovo),
    url(r'^fornecedoresVisualizar/', views.fornecedoresVisualizar),
    url(r'^fornecedoresEditar/', views.fornecedoresEditar),
    url(r'^fornecedoresSalvar/', views.fornecedoresSalvar),
    url(r'^funcao/', views.funcaoHome),
    url(r'^funcaoNovo/', views.funcaoNovo),
    url(r'^funcaoVisualizar/', views.funcaoVisualizar),
    url(r'^funcaoSalvar/', views.funcaoSalvar),
    url(r'^clientes/', views.clientesHome),
    url(r'^clientesNovo/', views.clientesNovo),
    url(r'^clientesVisualizar/', views.clientesVisualizar),
    url(r'^clientesEditar/', views.clientesEditar),
    url(r'^orcamentos/', views.orcamentosHome),
    url(r'^estoque/', views.estoqueHome),
    url(r'^equipamentos/', views.equipamentosHome),
    url(r'^equipamentosNovo/', views.equipamentosNovo),
    url(r'^equipamentosVisualizar/', views.equipamentosVisualizar),
    url(r'^equipamentosSalvar/', views.equipamentosSalvar),
    url(r'^contas/', views.contasHome),
]