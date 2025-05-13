from django.shortcuts import render
from .models import Cargo

# Create your views here.
def menu(request):
    return render(request, 'home.html')

def cargos(request):
    datcargos = Cargo.objects.all()
    query = request.GET.get('q',None)
    print(query)
    if query:
        datcargos = Cargo.objects.filter(name__icontains=query)
    else:
        datcargos = Cargo.objects.all()
        context = {'datcargos': datcargos, 'title': 'Listado de cargos'} 
    return render(request, 'cargos/cargoslist.html', context)