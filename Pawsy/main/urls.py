from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'animals', views.AnimalView, basename='animal')
router.register(r'adoption-requests', views.AdoptionRequestView, basename='adoption-request')
router.register(r'volunteers', views.VolunteerView, basename='volunteer')

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('animals/', views.AnimalListView.as_view(), name='animal_list'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('volunteers/', views.VolunteerListView.as_view(), name='volunteer_list'),
    path('volunteers/<int:pk>/', views.VolunteerDetailView.as_view(), name='volunteer_detail'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
