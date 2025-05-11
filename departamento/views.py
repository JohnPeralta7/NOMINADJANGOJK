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
    ...

def delete(request, id):
    ...