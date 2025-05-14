from django.shortcuts import render, redirect
from .models import Departamentos
from .forms import DepartamentoForm

# Create your views here.
def listado(request):
    query = request.GET.get('q') # None
    departamentos = Departamentos.objects.all() #[{'id' : 1, 'description' : 'TICS'}, {'id' : 2, 'description' : 'Inspector'}]
    if query:
        departamentos = Departamentos.objects.filter(description__icontains=query)
    return render(request, 'departamento/listado.html', {
        'departamentos' : departamentos,
        'title' : 'Listado departamental'
    })

def create(request):
    context = {'title': 'Ingresar Departamento'}
    if request.method == 'GET':
        form = DepartamentoForm()
        context['form'] = form #Creo una llave form y tomara de valor mi objeto formulario de departamento
        return render(request, 'departamento/create.html', context ) #{'title': 'Ingresar Departamento', 'form' : form}
    else:
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departamento:listado')
        else:
            context['form'] = form
            return render(request, 'departamento/create.html')

def update(request, id):
    context = {'title' : 'Actualizar Departamento'}
    departamento = Departamentos.objects.get(pk=id)
    if request.method == 'GET':
        form = DepartamentoForm(instance=departamento)
        context['form'] = form
        return render(request, 'departamento/update.html', context)
    else:
        form = DepartamentoForm(request.POST, instance=departamento)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('departamento:listado')
        #tengo que implementarle lo que hara sino funciona

def delete(request, id):
    departamento=None
    try:
        departamento = Departamentos.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Eliminar :','departamento':departamento,'error':''}
            return render(request, 'departamento/delete.html',context)  
        else: 
            departamento.delete()
            return redirect('departamento:listado')
    except:
        context = {'title':'Departamento info','departamento':departamento,'error':'Error al eliminar departamento'}
        return render(request, 'departamento/delete.html',context)