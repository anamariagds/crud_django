from django.forms import ModelForm
from .models import Conta

class contasForm(ModelForm):
    class Meta:
        model = Conta
        fields = ['descricao', 'valor', 'observacao', 'data', 'categoria']