from django.shortcuts import render

# Create your views here.

from typing import Dict

from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from App.models import Remeras, Pantalones, Calzado
from App.forms import RemerasFormulario, CalzadoFormulario, PantalonesFormulario

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def entregables(request):

    return render(request, "AppCoder/entregables.html")

# Formulario a mano
# def crear_curso(request):
#       if request.method == 'POST':
#             data_formulario: Dict = request.POST
#             curso = Curso(nombre=data_formulario['nombre'], comision=data_formulario['comision'])
#             curso.save()
#             return render(request, "AppCoder/inicio.html")
#       else:  # GET
#             return render(request, "AppCoder/form_curso.html")

# Vistas de Cursos

def remeras(request):
    remeras = remeras.objects.all()
    return render(request, "AppCoder/remeras.html", {'remeras': remeras})

def crear_remeras(request):
    if request.method == 'POST':
        formulario = RemerasFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            remeras = Remeras(color=data['color'],modelo=data['modelo'], talle=data['talle'])
            remeras.save()
            return render(request, "AppCoder/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = RemerasFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_remeras.html", {"formulario": formulario})

def busqueda_remeras(request):
    return render(request, "AppCoder/form_busqueda_remeras.html")

def buscar_remeras(request):
    if request.GET["modelo"]:
        modelo = request.GET["modelo"]
        remeras = Remeras.objects.filter(modelo__icontains=modelo)
        return render(request, "AppCoder/remeras.html", {'remeras': remeras})
    elif request.GET["talle"]:
        talle = request.GET["talle"]
        remeras = Remeras.objects.filter(talle__incontains=talle)
    else:
        return render(request, "AppCoder/remeras.html", {'remeras': [remeras]})

# Vistas de Profesores

def pantalones(request):
    pantalones = Pantalones.objects.all()  # trae todos los pantalones
    contexto = {"pantalones": pantalones}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppCoder/pantalones.html", contexto)

def eliminar_pantalones(request, id):
    pantalones = pantalones.objects.get(id=id)
    borrado_id = pantalones.id
    pantalones.delete()
    url_final = f"{reverse('pantalones')}?borrado={borrado_id}"

    return redirect(url_final)

def crear_pantalones(request):
    if request.method == 'POST':
        formulario = PantalonesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            pantalones = Pantalones(**data)
            # profesor = Profesor(apellido=data['apellido'], nombre=data['nombre'])
            pantalones.save()
            return redirect(reverse('pantalones'))
    else:  # GET
        formulario = PantalonesFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_profesor.html", {"formulario": formulario})

def editar_pantalones(request, id):
    # Recibe param pantalones id, con el que obtenemos el profesor
    pantalones = Pantalones.objects.get(id=id)

    if request.method == 'POST':
        PantalonesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            pantalones.color = data['color']
            pantalones.talle = data['talle']
            pantalones.modelo = data['modelo']

            pantalones.save()

            return redirect(reverse('pantaloneses'))
    else:  # GET
        inicial = {
            'color': pantalones.color,
            'talle': pantalones.talle,
            'modelo': pantalones.modelo,
        }
        formulario = PantalonesFormulario(initial=inicial)
    return render(request, "AppCoder/form_pantalones.html", {"formulario": formulario})

# Vistas de Estudiantes

class CalzadoListView(ListView):
    model = Calzado
    template_name = 'AppCoder/calzado.html'

class CalzadoCreateView(CreateView):
    model = Calzado
    fields = ['color', 'talle', 'modelo']
    success_url = reverse_lazy('calzado')

class CalzadoUpdateView(UpdateView):
    model = Calzado
    fields = ['color', 'talle','modelo']
    success_url = reverse_lazy('estudiantes')

class CalzadoDeleteView(DeleteView):
    pass
