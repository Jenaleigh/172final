from django import path
from petapp import views

urlpatterns = [
    path('', views.index, name='index'),
]