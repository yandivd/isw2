from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import UpdateView

# Create your views here.
@login_required
def home(request):
    return render(request, 'main/index.html')

# Historias Clinicas CRUD
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

def verHC(request,pk):
    paciente = get_object_or_404(Paciente, id=pk)
    hc = get_object_or_404(Historia_clinica, id=pk)
    data = {
        "formP" : PacienteForm(instance=paciente),
        "formHC" : HCForm(instance=hc),
    }
    # if request.method=='POST':
    #     formulario = PacienteForm(data=request.POST, instance=paciente, files=request.FILES)
    #     if formulario.is_valid():
    #         formulario.save()
    #         messages.success(request,"Modificada Correctamente")
    #         return redirect(to='home') #te redirige al listado de productos ya editados
    #     else:
    #         data["formP"]=formulario

    return render(request,'gestion/hc/view.html', data)

#Cosas de los Pacientes
@permission_required('main.add_paciente')
def crearPaciente(request):
    
    data = {
        'form': PacienteForm,
    }

    return render(request, 'gestion/pacientes/create.html', data)