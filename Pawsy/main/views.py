from django.shortcuts import render, get_object_or_404
from .models import Animal

def home(request):
    # Get a few featured animals (e.g., the 3 most recent ones)
    featured_animals = Animal.objects.filter(status__name__contains='Looking').order_by('-data_arrived')[:3]
    return render(request, 'home.html', {'featured_animals': featured_animals})

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        from .models import AdoptionRequest
        adoption_request = AdoptionRequest(
            animal=animal,
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        adoption_request.save()

        from django.contrib import messages
        messages.success(request, f"Thank you for your interest in adopting {animal.name}! We'll contact you soon.")

    return render(request, 'animal_detail.html', {'animal': animal})
