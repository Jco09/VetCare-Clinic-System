from rest_framework import serializers
from .models import Owner, Pet, Appointment

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    pet_name = serializers.CharField(source='pet.name', read_only=True)
    owner_name = serializers.CharField(source='pet.owner.name', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'pet', 'pet_name', 'owner_name', 'date_time', 'reason', 'status']