from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/lista.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado:lista')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/formulario.html', {'form': form})

def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado:lista')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/formulario.html', {'form': form})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado:lista')
    return render(request, 'empleado/confirmar_eliminar.html', {'empleado': empleado})