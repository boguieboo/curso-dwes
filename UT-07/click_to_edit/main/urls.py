from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/contact/1/edit', views.edit_name, name='edit_name'),
    path('save/', views.save_name, name='save_name'),
]
