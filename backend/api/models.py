from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return f"{self.name} ({self.species})"

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default="Scheduled")

    def __str__(self):
        return f"{self.pet.name} - {self.date_time}"