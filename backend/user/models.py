from django.db import models
from django.contrib.auth.models import User
from restaurant.models import RestaurantTruck

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

class Favorite(models.Model):
    user = models.ForeignKey(
        UserProfile,
        related_name="user_favorite",
        on_delete=models.CASCADE,
        null=True
    )
    favorite = models.ForeignKey(
        RestaurantTruck,
        related_name="favorite",
        on_delete=models.CASCADE,
        null=True
    )
