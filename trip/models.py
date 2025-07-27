from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

user = get_user_model()

# Create your models here.

class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)#country code i.e USA = US
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(user, on_delete=models.CASCADE,related_name='trips')
    

    def __str__(self):
        return f"{self.city} ({self.start_date})"
    
class Note(models.Model):
    EXCURSION = (
        ("event", "Event"),
        ("dining", "Dining"),
        ("exprience", "Experience"),
        ("general", "General"),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=EXCURSION, default='general')
    img = models.ImageField(upload_to='notes/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.rating}/5"