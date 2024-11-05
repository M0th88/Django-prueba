from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscripcion
from .forms import InscripcionForm  

# Listar inscripciones
def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'seminarios/listar.html', {'inscripciones': inscripciones})


def agregar_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'seminarios/agregar.html', {'form': form})


def modificar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'seminarios/modificar.html', {'form': form})

def eliminar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('listar_inscripciones')
    return render(request, 'seminarios/eliminar.html', {'inscripcion': inscripcion})
