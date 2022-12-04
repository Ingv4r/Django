from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('filling_form', views.filling_form, name='form'),
    path('create', views.create, name='create')
]