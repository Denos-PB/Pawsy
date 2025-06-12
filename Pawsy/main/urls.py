from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:animal_id>/', views.animal_detail, name='animal_detail'),
]
