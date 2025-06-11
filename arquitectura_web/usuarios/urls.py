from django.urls import path
from .views import ( login_view, 
                    register_view, 
                    crear_carpeta, 
                    lista_carpetas, 
                    subir_archivo, 
                    ver_archivos, 
                    crear_materia, 
                    lista_materias,
                    buscar_carpetas )
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('carpetas/', lista_carpetas, name='lista_carpetas'),
    path('carpetas/nueva/', crear_carpeta, name='crear_carpeta'),
    path('carpetas/<int:carpeta_id>/subir/', subir_archivo, name='subir_archivo'),
    path('carpetas/<int:carpeta_id>/archivos/', ver_archivos, name='ver_archivos'),      
    path('materias/', lista_materias, name='lista_materias'),
    path('materias/nueva/', crear_materia, name='crear_materia'),
    path('carpetas/buscar/', buscar_carpetas, name='buscar_carpetas'),
]
