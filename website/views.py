from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from helloworld.models import Funcionario
from .forms import InsereFuncionarioForm
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
    context_object_name = 'funcionarios'
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