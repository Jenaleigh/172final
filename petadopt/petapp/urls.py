from django.urls import path
from petapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name='pets'),
    path('newPet/', views.newPet, name='newpet'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
