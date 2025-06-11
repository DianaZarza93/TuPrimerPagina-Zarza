# Python y Django

## Curso

Comision 75905

Profesor: Estevan H. Acevedo

## Alumno

Nombre: Diana Zarza

## 🏛 Web de Arquitectura - Proyecto Final Django

Este es mi proyecto final desarrollado en Django, inspirado visualmente en *Bloodborne*. Permite a estudiantes de arquitectura guardar carpetas por materia, subir y descargar archivos, y acceder desde cualquier dispositivo.

---

## 🎯 Objetivos del Proyecto

- Crear una web con Django usando el patrón **MVT**
- Utilizar **herencia de plantillas HTML**
- Tener **3 modelos** en la base de datos
- Crear formularios para insertar datos en cada modelo
- Implementar un formulario para **buscar** en la base de datos
- Añadir autenticación de usuarios

---

## 🛠 Tecnologías utilizadas

- Python 3.13
- Django 5.2.3
- HTML + CSS personalizado estilo *Bloodborne*
- SQLite3 (base de datos por defecto de Django)

---

## 🧩 Modelos

1. **Materia**
   - Nombre
   - Cuatrimestre

2. **Carpeta**
   - Nombre
   - Usuario (relación con usuario de Django)
   - Materia (relación con `Materia`)
   - Fecha de creación

3. **Archivo**
   - Archivo (documento subido)
   - Carpeta (relación con `Carpeta`)
   - Nombre original
   - Fecha de subida

---

## 🧪 Funcionalidades implementadas

✅ Registro e inicio de sesión de usuarios  
✅ Creación de materias  
✅ Creación de carpetas vinculadas a materias  
✅ Subida de archivos por carpeta  
✅ Descarga de archivos  
✅ Búsqueda de carpetas por nombre  
✅ Herencia de plantillas con `base.html`  
✅ Estilo gótico inspirado en *Bloodborne*

---
PD: Falta varias cosas por trabajar pero al menos es hasta donde llegue, para la entrega final va a estar mas prolijo.
