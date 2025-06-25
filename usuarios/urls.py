from django.urls import path
from .views import ( login_view, register_view, buscar_carpetas, eliminar_archivo )
from .views import ( CarpetaListView, CarpetaCreateView, ArchivoCreateView, ArchivoListView, CarpetaDeleteView)
from .views import ( MateriaListView, MateriaDetailView, MateriaCreateView, MateriaDeleteView)
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('carpetas/', CarpetaListView.as_view(), name='lista_carpetas'),
    path('carpetas/nueva/', CarpetaCreateView.as_view(), name='crear_carpeta'),
    path('carpetas/<int:carpeta_id>/subir/', ArchivoCreateView.as_view(), name='subir_archivo'),
    path('carpetas/<int:carpeta_id>/archivos/', ArchivoListView.as_view(), name='ver_archivos'),
    path('carpetas/buscar/', buscar_carpetas, name='buscar_carpetas'),
    path('carpetas/<int:pk>/eliminar/', CarpetaDeleteView.as_view(), name='eliminar_carpeta'),
    path('carpetas/<int:carpeta_id>/archivo/<int:pk>/eliminar/', eliminar_archivo, name='eliminar_archivo'),
    path('materias/', MateriaListView.as_view(), name='lista_materias'),
    path('materias/nueva/', MateriaCreateView.as_view(), name='crear_materia'),
    path('materias/<int:pk>/', MateriaDetailView.as_view(), name='detalle_materia'),  # 👈 esta es clave
    path('materias/<int:pk>/eliminar/', MateriaDeleteView.as_view(), name='eliminar_materia'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]
