from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_madlib, name='create_madlib'),
    path('about/', views.about, name='about'),
]
