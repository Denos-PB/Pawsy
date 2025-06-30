from .serializer import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

class AnimalView(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AdoptionRequestView(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ReferenceDataView(mixins.ListModelMixin,
                       generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GenderView(ReferenceDataView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class ColorView(ReferenceDataView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizeView(ReferenceDataView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class StatusView(ReferenceDataView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class AnimalBreedView(ReferenceDataView):
    queryset = AnimalBreed.objects.all()
    serializer_class = AnimalBreedSerializer

class VolunteerView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = VolunteerSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            return Volunteer.objects.filter(status=VolunteerStatusChoice.APPROVED)
        return Volunteer.objects.all()


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_animals'] = Animal.objects.filter(status__name='Available').order_by('?')[:3]
        return context


class AnimalListView(ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animals'

    def get_queryset(self):
        return Animal.objects.filter(status__name='Available')


@method_decorator(csrf_protect, name='dispatch')
class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animal_detail.html'
    context_object_name = 'animal'

    def post(self, request, *args, **kwargs):
        animal = self.get_object()

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and email and phone:
            adoption_request = AdoptionRequest.objects.create(
                animal=animal,
                name=name,
                email=email,
                phone=phone,
                message=message
            )

            messages.success(request, f"Your adoption request for {animal.name} has been submitted successfully!")
            return redirect('animal_detail', pk=animal.id)
        else:
            messages.error(request, "Please fill out all required fields.")
            return self.get(request, *args, **kwargs)


class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'volunteer_list.html'
    context_object_name = 'volunteers'

    def get_queryset(self):
        return Volunteer.objects.filter(status=VolunteerStatusChoice.APPROVED)
