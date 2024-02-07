from django.forms import ModelForm
from app.models import Registro



class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['protocolo', 'solicitacao', 'a', 'c', 'r', 'nc', 'lm']









