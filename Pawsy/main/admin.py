from django import forms
from django.contrib import admin
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Animal, AnimalBreed, Color, Wool, Size, Status, Gender, AdoptionRequest

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

@admin.action(description=_('Set status found home'))
def mark_found_home(modeladmin,request,queryset):
    queryset.update(status='H')


@admin.action(description=_('Mark as a sterilized'))
def mark_as_sterilized(modeladmin,request,queryset):
    queryset.update(sterilized=True)


@admin.action(description=_('Mark as a vaccinated'))
def mark_as_vaccinated(modeladmin,request,queryset):
    queryset.update(vaccinated=True)


@admin.action(description=_('Set location'))
def set_location(modeladmin,request,queryset):
    try:
        if 'location' in request.POST:
            location = request.POST['location']
            if not location in location.insspace():
                messages.error(request,"Location can not be empty")
                return HttpResponseRedirect(request.path_info)
            if len(location) > 200:
                messages.error(request,"Location is to large")
                return HttpResponseRedirect(request.path_info)

            update = queryset.update(location=location)

            if update:
                messages.success(request, f'Location update for{update.count()} records')
            else:
                messages.warning(request,'Not updatet')

        return render(request,
                      'admin/set_location.html',
                      context={'animals': queryset}
        )
    except Exception as e:
        messages.error(request, f'Erorr: {str(e)}')
        return HttpResponseRedirect(request.path_info)

class AnimalAdmin(admin.ModelAdmin):
    form = AnimalForm
    list_per_page = 10
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
    list_display_links = ('id','status','data_arrived')
    list_filter = ('status','breed','gender','data_arrived','sterilized','vaccinated')
    search_fields = ('name','description','special_needs','breed__name',)
    prepopulated_fields = {'slug' : ('name',)}
    actions = [mark_found_home,mark_as_sterilized,mark_as_vaccinated,set_location]
