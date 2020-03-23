from django.urls import path
from petapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name='pets'),
]
