from django.shortcuts import render
from .models import Departamentos

# Create your views here.
def listado(request):
    query = request.GET.get('q')
    departamentos = Departamentos.objects.all()
    if query:
        departamentos = Departamentos.objects.filter(description__icontains=query)
    return render(request, 'departamento/listado.html', {
        'departamentos' : departamentos,
        'title' : 'Listado departamental'
    })