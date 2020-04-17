"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from website.views import IndexTemplateView, FuncionarioCreateView, FuncionarioListView, FuncionarioFilterListView, FuncionarioUpdateView, FuncionarioDeleteView

app_name = 'website'

urlpatterns = [

    path('', IndexTemplateView.as_view(), name='index'),
    path('funcionarios/', views.funcionario_list, name='lista_funcionario'),
    # path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionario'),
    # path('funcionarios/<filter>', FuncionarioFilterListView.as_view(), name='lista_funcionario_filtro'),
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),

    # path('funcionarios/<int:ano>/', views.funcionarios_por_ano),
]
