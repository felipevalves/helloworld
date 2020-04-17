from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from helloworld.models import Funcionario
from .forms import InsereFuncionarioForm, ConsultaFuncionarioForm
# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'website/index.html'

class FuncionarioCreateView(CreateView):
    template_name = 'website/cria.html'
    model = Funcionario
    form_class = InsereFuncionarioForm
    # reverse_lazy traduz a View em URL
    success_url = reverse_lazy('website:lista_funcionario')


class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    # fields = ['nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao']
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")

class FuncionarioDeleteView(DeleteView):
    template_name = 'website/exclui.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionario")

class FuncionarioListView(ListView):
    template_name = 'website/lista.html'
    model = Funcionario
    form_class = ConsultaFuncionarioForm
    # list_funcionarios = Funcionario.objetos.order_by('nome')
    # context = {'funcionarios': list_funcionarios}
    context_object_name = 'funcionarios'

class FuncionarioFilterListView(ListView):
    template_name = 'website/lista.html'
    model = Funcionario
    form_class = ConsultaFuncionarioForm
    list_funcionarios = Funcionario.objetos.filter(nome='Felipe')
    context_object_name = 'funcionarios'

def funcionario_list(request):

    # if request.method == "POST":
    form = Funcionario(nome=request.GET.get('nome', ''))
    # else:
    #     form = Funcionario()

    funcionarios = Funcionario.objetos\
        .filter(Q(nome__contains=form.nome) | Q(sobrenome__contains=form.nome))\
        .order_by('nome')

    return render(request, 'website/lista.html', {'funcionarios': funcionarios, 'filtro': 'filtro', 'form': form})

# funcionando ok
# def funcionario_list(request):
#     filtro = ''
#     if request.method == "POST":
#         filtro = request.POST.get('filtro')
#     funcionarios = Funcionario.objetos.filter(Q(nome__contains=filtro) | Q(sobrenome__contains=filtro)).order_by('nome')
#
#     return render(request, 'website/lista.html', {'funcionarios': funcionarios, 'filtro': filtro})



# def criar_funcionario(request, pk):
#
#     if request.method == 'POST':
#         form = FormularioDeCriacao(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('list_view'))
#
#     else:
#         return render(request, templates/form.html, {'form': form})