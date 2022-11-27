from django import forms
from .models import *

class HCForm(forms.ModelForm):

    class Meta:
        model=Historia_clinica
        fields='__all__'

class FormularioForm(forms.ModelForm):

    class Meta:
        model=Formulario
        fields='__all__'