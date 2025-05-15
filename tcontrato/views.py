from django.shortcuts import render, redirect
from .models import TipoContrato
from .forms import TipoContratoForm

# Create your views here.

def tcontratos(request):
    dattcontrato = TipoContrato.objects.all()
    query = request.GET.get('q')
    if query:
        dattcontrato = TipoContrato.objects.filter(description__icontains=query)
    return render(request, 'tcontrato/listado.html', {
        'dattcontrato': dattcontrato, 
        'title': 'Listado de contratos'})

def tcontrato_create(request):
    context = {'title' : 'Ingresar tipo contrato'}
    if request.method == 'GET':
        form = TipoContratoForm()
        context['form'] = form
        return render(request, 'tcontrato/create.html', context)
    else:
        form = TipoContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('t_contrato:listado')
        else:
            context['form'] = form
            return render(request, 'tcontrato/create.html')

def tcontrato_update(request, id):
    context = {'title' : 'Actualizar tcontrato'}
    tcontrato = TipoContrato.objects.get(id=id)
    if request.method == 'GET':
        form = TipoContratoForm(instance=tcontrato)
        context['form'] = form
        return render(request, 'tcontrato/update.html', context)
    else:
        form = TipoContratoForm(request.POST, instance=tcontrato)
        if form.is_valid():
            form.save()
            return redirect('t_contrato:listado')
        else:
            context['form'] = form
            return render(request, 'tcontrato/update.html')

def tcontrato_delete(request, id):
    from django.core.exceptions import ObjectDoesNotExist
    tcontrato = None
    try:
        tcontrato = TipoContrato.objects.get(id=id)
        if request.method == 'GET':
            context = {'title' : 'Tipo de Contrato a Eliminar', 'tcontrato' : tcontrato, 'error' : ''}
            return render(request, 'tcontrato/delete.html', context)
        else:
            tcontrato.delete()
            return redirect('t_contrato:listado')
    except ObjectDoesNotExist:
        context = {'title' : 'Tipo de contrato a Eliminar', 'tcontrato' : tcontrato, 'error' : 'Error al eliminar el tipo de contrato'}
        return render(request, 'tcontrato/delete.html', context)