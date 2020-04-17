from django import forms
from helloworld.models import Funcionario
class InsereFuncionarioForm(forms.ModelForm):

    # campos que estarão no form
    chefe = forms.BooleanField(
        label='Chefe?',
        required=False
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        model = Funcionario

        # campos que estarão no form
        fields = ['nome', 'sobrenome', 'cpf', 'remuneracao']
        # campos que não estarão no form
        exclude = ['tempo_de_servico']

class ConsultaFuncionarioForm(forms.Form):
    class Meta:
        model = Funcionario

        # campos que estarão no form
        fields = ['nome']
        # campos que não estarão no form
        # exclude = ['tempo_de_servico']

# class InsereFuncionarioForm(forms.Form):
#     nome = forms.CharField(
#         required=True,
#         max_length=255
#     )
#
#     sobrenome = forms.CharField(
#         required=True,
#         max_length=255
#     )
#     cpf =forms.CharField(
#         required=True,
#         max_length=14
#     )
#
#     tempo_de_servico = forms.IntegerField(
#         required=True
#     )
#
#     remuneracao = forms.DecimalField()