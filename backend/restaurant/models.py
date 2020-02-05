from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile

# Create your models here.

class RestaurantTruck(models.Model):
    restaurant = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    rating = models.IntegerField()
    owner = models.OneToOneField(
        User,
        related_name="owner",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return(f"{self.restaurant} | {self.phone} | {self.email}")

class Menu(models.Model):
    dish = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    restaurant = models.ForeignKey(
        RestaurantTruck,
        related_name="restaurant",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return(f"{self.dish}")

class Review(models.Model):
    stars = models.IntegerField()
    comment = models.TextField()
    truck_review = models.OneToOneField(
        RestaurantTruck,
        related_name="truck_review",
        on_delete=models.CASCADE,
        null=True
    )
    customer_voice = models.ForeignKey(
        UserProfile,
        related_name="customer_voice",
        on_delete=models.CASCADE,
        null=True
    )

