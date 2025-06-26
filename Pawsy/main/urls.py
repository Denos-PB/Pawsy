from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'animals', views.AnimalView, basename='animal')
router.register(r'adoption-requests', views.AdoptionRequestView, basename='adoption-request')
router.register(r'volunteers', views.VolunteerView, basename='volunteer')

# Define URL patterns
urlpatterns = [
    # Template-based URLs
    path('', views.HomeView.as_view(), name='home'),
    path('animals/', views.AnimalListView.as_view(), name='animal_list'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),

    # API URLs - these will be accessible via /api/ prefix in the project's main urls.py
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
