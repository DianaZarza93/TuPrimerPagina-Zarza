from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Materia, Carpeta, Archivo
from .forms import MateriaForm, CarpetaForm, ArchivoForm
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator


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


class MateriaListView(ListView):
    model = Materia
    template_name = 'usuarios/materia_list.html'
    context_object_name = 'materias'

class MateriaDetailView(DetailView):
    model = Materia
    template_name = 'usuarios/materia_detail.html'

class MateriaCreateView(CreateView):
    model = Materia
    fields = ['nombre', 'cuatrimestre', 'fecha_creacion']
    template_name = 'usuarios/materia_form.html'
    success_url = reverse_lazy('lista_materias')

class MateriaDeleteView(DeleteView):
    model = Materia
    template_name = 'usuarios/materia_confirm_delete.html'
    success_url = reverse_lazy('lista_materias')

# Vista para listar carpetas del usuario
class CarpetaListView(LoginRequiredMixin, ListView):
    model = Carpeta
    template_name = 'usuarios/lista_carpetas.html'
    context_object_name = 'carpetas'

    def get_queryset(self):
        return Carpeta.objects.filter(usuario=self.request.user)

# Vista para crear una carpeta
class CarpetaCreateView(LoginRequiredMixin, CreateView):
    model = Carpeta
    form_class = CarpetaForm
    template_name = 'usuarios/crear_carpeta.html'
    success_url = reverse_lazy('lista_carpetas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

# Vista para subir archivo a una carpeta
class ArchivoCreateView(LoginRequiredMixin, CreateView):
    model = Archivo
    form_class = ArchivoForm
    template_name = 'usuarios/subir_archivo.html'

    def form_valid(self, form):
        carpeta_id = self.kwargs['carpeta_id']
        carpeta = Carpeta.objects.get(id=carpeta_id, usuario=self.request.user)
        form.instance.carpeta = carpeta
        form.instance.nombre_original = form.instance.archivo.name
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ver_archivos', kwargs={'carpeta_id': self.kwargs['carpeta_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carpeta'] = Carpeta.objects.get(id=self.kwargs['carpeta_id'], usuario=self.request.user)
        return context

# Vista para ver archivos de una carpeta
class ArchivoListView(LoginRequiredMixin, ListView):
    model = Archivo
    template_name = 'usuarios/ver_archivos.html'
    context_object_name = 'archivos'

    def get_queryset(self):
        carpeta_id = self.kwargs['carpeta_id']
        return Archivo.objects.filter(carpeta__id=carpeta_id, carpeta__usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carpeta'] = Carpeta.objects.get(id=self.kwargs['carpeta_id'], usuario=self.request.user)
        return context
