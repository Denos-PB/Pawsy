from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Name cannot be empty'}},
            'age': {'error_messages': {'invalid': 'Age must be a number'}},
            'size': {'required': False},}
        depth = 1

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'
        read_only_fields = ('slug',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        read_only_fields = ('slug',)

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Size cannot be empty'}},
        }
class WoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wool
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Wool cannot be empty'}},
        }

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Status cannot be empty'}},
        }
class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Breed cannot be empty'}},
        }
class AdoptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionRequest
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Adoption request cannot be empty'}},
            'phone': {'error_messages': {'blank': 'Phone number cannot be empty'}},
            'email': {'error_messages': {'blank': 'Email cannot be empty'}},
            'message': {'error_messages': {'blank': 'Message cannot be empty'}},
        }
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Volunteer name cannot be empty'}},
            'phone': {'error_messages': {'blank': 'Phone number cannot be empty'}},
            'email': {'error_messages': {'blank': 'Email cannot be empty'}},
        }
class VolunteerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerRequest
        fields = '__all__'
        read_only_fields = ('slug',)
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Volunteer name cannot be empty'}},
            'phone': {'error_messages': {'blank': 'Phone number cannot be empty'}},
            'email': {'error_messages': {'blank': 'Email cannot be empty'}},
            'message': {'error_messages': {'blank': 'Message cannot be empty'}},

        }
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
        read_only_fields = ('slug',)
