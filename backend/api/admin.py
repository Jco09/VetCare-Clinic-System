from django.contrib import admin
from .models import Owner, Pet, Appointment

admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Appointment)