from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    account = models.OneToOneField(
        User,
        related_name="account",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return(f"{self.username} | {self.email}")

class RestaurantTruck(models.Model):
    restaurant = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    owner = models.OneToOneField(
        User,
        related_name="owner",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return(f"{self.restaurant} | {self.phone} | {self.email}")

class Favorite(models.Model):
    user = models.ForeignKey(
        UserProfile,
        related_name="user",
        on_delete=models.CASCADE,
        null=True
    )
    favorite = models.ForeignKey(
        RestaurantTruck,
        related_name="favorite",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return(f"{self.favorite}")

class Menu(models.Model):
    dish = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    restaurant_name = models.ForeignKey(
        RestaurantTruck,
        related_name="restaurant_name",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return(f"{self.dish}")

class MenuPage(models.Model):
    image = models.ImageField(upload_to='images/')
    restaurant_menu = models.ForeignKey(
        RestaurantTruck,
        related_name="restaurant_menu",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return(f"{self.image} | {self.restaurant_menu}")

class Review(models.Model):
    stars = models.IntegerField(default=3)
    comment = models.TextField()
    truck_review = models.ForeignKey(
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

    def __str__(self):
        return(f"{self.truck_review} | {self.stars}")
