from django.shortcuts import render
from django.http import HttpResponse
from .models import get_user, update_user

# Simulación de "base de datos"
CURRENT_NAME = "Juan Pérez"

def index(request):
    user = get_user()
    return render(request, "index.html", {"user": user})

def display_name(request):
    user = get_user()
    return render(request, "partials/name_display.html", {"user": user})

def edit_name(request):
    user = get_user()
    return render(request, "partials/edit_form.html", {"user": user})


def save_name(request):
    user = update_user(
        request.POST.get("firstName"),
        request.POST.get("lastName"),
        request.POST.get("email"),
    )
    return render(request, "partials/name_display.html", {"user": user})