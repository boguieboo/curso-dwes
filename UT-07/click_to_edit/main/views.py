from django.shortcuts import render
from django.http import HttpResponse

# Simulación de "base de datos"
CURRENT_NAME = "Juan Pérez"

def index(request):
    return render(request, "index.html", {"name": CURRENT_NAME})


def edit_name(request):
    return render(request, "partials/edit_form.html", {"name": CURRENT_NAME})


def save_name(request):
    global CURRENT_NAME
    CURRENT_NAME = request.POST.get("name", CURRENT_NAME)
    return render(request, "partials/name_display.html", {"name": CURRENT_NAME})
