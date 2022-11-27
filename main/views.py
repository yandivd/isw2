from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import UpdateView

# Create your views here.
###Historias CLinicas###
@login_required
def home(request):
    return render(request, 'main/index.html')

# Historias Clinicas CRUD
@login_required
def hclistar(request):
    try:
        estadoT = Estado.objects.get(nombre='Activo')
        historias = Historia_clinica.objects.all().filter(estado=estadoT)
        return render(request, 'gestion/hc/hclist.html',{
        'historias': historias,
    })
    except Exception as e:
        print(e)
    return render(request, 'gestion/hc/hclist.html')

@permission_required('main.add_historia_clinica')
def crearHC(request):
    
    data = {
        'form': HCForm,
    }
    
    if request.method=='POST':
        formulario=HCForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            # messages.success(request,"Modificada Correctamente")
            return redirect(to='home') #te redirige al listado de productos ya editados
        else:
            data["form"]=formulario
    return render(request, 'gestion/hc/create.html', data)

def verHC(request,id):
    hc = get_object_or_404(Historia_clinica, id=id)
    data = {
        "formHC" : HCForm(instance=hc),
    }

    return render(request,'gestion/hc/view.html', data)

###Creacion de Formulario de los Pacientes###
def createFormulario(request):
    data={
        'form': FormularioForm,
    }
    if request.method=='POST':
        formulario=FormularioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # messages.success(request,"Modificada Correctamente")
            return redirect(to='home') #te redirige al listado de productos ya editados
        else:
            data["form"]=formulario
    return render(request, 'formulario/create.html', data)