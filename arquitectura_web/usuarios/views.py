from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Materia, Carpeta, Archivo
from .forms import MateriaForm, CarpetaForm, ArchivoForm
from django.db.models import Q



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})


@login_required
def crear_carpeta(request):
    if request.method == 'POST':
        form = CarpetaForm(request.POST)
        if form.is_valid():
            carpeta = form.save(commit=False)
            carpeta.usuario = request.user
            carpeta.save()
            return redirect('lista_carpetas')
    else:
        form = CarpetaForm()
    return render(request, 'usuarios/crear_carpeta.html', {'form': form})

@login_required
def lista_carpetas(request):
    carpetas = Carpeta.objects.filter(usuario=request.user)
    return render(request, 'usuarios/lista_carpetas.html', {'carpetas': carpetas})

@login_required
def subir_archivo(request, carpeta_id):
    carpeta = Carpeta.objects.get(id=carpeta_id, usuario=request.user)

    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.carpeta = carpeta
            archivo.nombre_original = archivo.archivo.name
            archivo.save()
            return redirect('ver_archivos', carpeta_id=carpeta.id)
    else:
        form = ArchivoForm()

    return render(request, 'usuarios/subir_archivo.html', {'form': form, 'carpeta': carpeta})

@login_required
def ver_archivos(request, carpeta_id):
    carpeta = Carpeta.objects.get(id=carpeta_id, usuario=request.user)
    archivos = carpeta.archivo_set.all()
    return render(request, 'usuarios/ver_archivos.html', {'carpeta': carpeta, 'archivos': archivos})

@login_required
def crear_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_materias')
    else:
        form = MateriaForm()
    return render(request, 'usuarios/crear_materia.html', {'form': form})

@login_required
def lista_materias(request):
    materias = Materia.objects.all()
    return render(request, 'usuarios/lista_materias.html', {'materias': materias})

@login_required
def buscar_carpetas(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Carpeta.objects.filter(
            Q(nombre__icontains=query),
            usuario=request.user  # solo sus carpetas
        )

    return render(request, 'usuarios/buscar_carpetas.html', {
        'resultados': resultados,
        'query': query,
    })
