from django.shortcuts import render
from .models import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'main/index.html')

@login_required
def hclistar(request):
    estadoT = Estado.objects.get(nombre='Activo')
    historias = Historia_clinica.objects.all().filter(estado=estadoT)
    return render(request, 'gestion/hc/hclist.html',{
        'historias': historias,
    })

@permission_required('main.add_historia_clinica')
def crearHC(request):
    
    data = {
        'form': HCForm,
    }

    return render(request, 'gestion/hc/create.html', data)

@permission_required('main.add_paciente')
def crearPaciente(request):
    
    data = {
        'form': PacienteForm,
    }

    return render(request, 'gestion/pacientes/create.html', data)