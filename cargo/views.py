#si usas .save(commit=False) indicas a django que no lo vas a mandar al BD, sino que lo guardas temporalmente como un objeto (como hemos estado viendo en poo) asi que asi podremos acceder a los atributos y los valores que el usuario puso :)
from django.shortcuts import render, redirect
from .models import Cargo
from .forms import CargoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def menu(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET': 
        return render(request, 'signup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cargo:cargos')
            except IntegrityError:
                return render(request, 'signup.html', {
            'form' : UserCreationForm,
            'error' : 'Usuario ya existee'
        })
        return render(request, 'signup.html', {
            'form' : UserCreationForm,
            'error' : 'No coincide la contraseña'
        })
            
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form' : AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form' : AuthenticationForm,
            'error' : 'Usuario o contraseña incorrecta'
    })
        else:
            login(request, user)
            return redirect('cargo:cargos')
        
          


@login_required
def cargos(request):
    datcargos = Cargo.objects.all()
    query = request.GET.get('q')
    if query:
        datcargos = Cargo.objects.filter(description__icontains=query)
    return render(request, 'cargos/cargoslist.html', {
        'datcargos': datcargos, 
        'title': 'Listado de cargos'})

@login_required
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

@login_required       
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
        
@login_required
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
    
@login_required
def signout(request):
    logout(request)
    return redirect('inicio') 
