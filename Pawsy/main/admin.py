from django import forms
from django.contrib import admin
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Animal, AnimalBreed, Color, Wool, Size, Status, Gender, AdoptionRequest

admin.site.register(AnimalBreed)
admin.site.register(Color)
admin.site.register(Wool)
admin.site.register(Size)
admin.site.register(Status)
admin.site.register(Gender)
admin.site.register(AdoptionRequest)


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

@admin.action(description=_('Set status found home'))
def mark_found_home(modeladmin, request, queryset):
    found_home_status = Status.objects.get(name='H')
    queryset.update(status=found_home_status)


@admin.action(description=_('Mark as a sterilized'))
def mark_as_sterilized(modeladmin, request, queryset):
    queryset.update(sterilized=True)


@admin.action(description=_('Mark as a vaccinated'))
def mark_as_vaccinated(modeladmin, request, queryset):
    queryset.update(vaccinated=True)


@admin.action(description=_('Set location'))
def set_location(modeladmin, request, queryset):
    try:
        if 'location' in request.POST:
            location = request.POST['location']

            if not location or location.isspace():
                messages.error(request,"Location can not be empty")
                return HttpResponseRedirect(request.path_info)

            if len(location) > 200:
                messages.error(request,"Location is too large")
                return HttpResponseRedirect(request.path_info)

            update = queryset.update(location=location)

            if update:
                messages.success(request, f'Location update for {update} records')
            else:
                messages.warning(request,'Not updated')

        return render(request,
                      'admin/set_location.html',
                      context={'animals': queryset}
        )
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return HttpResponseRedirect(request.path_info)

class AnimalAdmin(admin.ModelAdmin):
    form = AnimalForm
    list_per_page = 10
    readonly_fields = ('data_arrived',)
    date_hierarchy = 'data_arrived'
    list_display = (
        'id',
        'name',
        'age',
        'breed',
        'status',
        'sterilized',
        'vaccinated',
        'data_arrived'
    )
    list_display_links = ('id', 'status', 'data_arrived')
    list_filter = ('status', 'breed', 'gender', 'data_arrived', 'sterilized', 'vaccinated')
    search_fields = ('name', 'description', 'special_needs', 'breed__name',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name', 'age', 'sterilized', 'vaccinated')
    actions = [mark_found_home, mark_as_sterilized, mark_as_vaccinated, set_location]
admin.site.register(Animal, AnimalAdmin)
