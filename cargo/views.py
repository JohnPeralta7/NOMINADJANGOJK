from django.shortcuts import render, redirect
from .models import Cargo
from .forms import CargoForm

# Create your views here.
def menu(request):
    return render(request, 'home.html')

def cargos(request):
    datcargos = Cargo.objects.all()
    query = request.GET.get('q')
    if query:
        datcargos = Cargo.objects.filter(description__icontains=query)
    return render(request, 'cargos/cargoslist.html', {
        'datcargos': datcargos, 
        'title': 'Listado de cargos'})

def cargos_create(request):
    context = {'title' : 'Ingresar Cargo'}
    if request.method == 'GET':
        form = CargoForm()
        context['form'] = form
        return render(request, 'cargos/cargo_create.html', context)
    else:
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo:cargos')
        else:
            context['form'] = form
            return render(request, 'cargo/cargo_create.html')
        
def cargos_update(request, id):
    context = {'title' : 'Actualizar Cargo'}
    cargo = Cargo.objects.get(id=id)
    if request.method == 'GET':
        form = CargoForm(instance=cargo)
        context['form'] = form
        return render(request, 'cargos/cargo_create.html', context)
    else:
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo:cargos')
        else:
            context['form'] = form
            return render(request, 'cargo/cargo_create.html')
        

def cargos_delete(request, id):
    cargo = None
    try:
        cargo = Cargo.objects.get(id=id)
        if request.method == 'GET':
            context = {'title' : 'Cargo a Eliminar', 'cargo' : cargo, 'error' : ''}
            return render(request, 'cargos/cargo_delete.html', context)
        else:
            cargo.delete()
            return redirect('cargo:cargos')
    except:
        context = {'title' : 'Cargo a Eliminar', 'cargo' : cargo, 'error' : 'Error a eliminar el cargo'}
        return render(request, 'cargos/cargo_delete.html', context)