from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^colaboradores/', views.colaboradores),
    url(r'^colaboradoresNovo/', views.colaboradoresNovo),
    url(r'^funcao/', views.funcaoHome),
    url(r'^funcaoNovo/', views.funcaoNovo),
    url(r'^funcaoVisualizar/', views.funcaoVisualizar),
    url(r'^funcaoSalvar/', views.funcaoSalvar),
]