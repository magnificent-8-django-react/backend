from django.contrib import admin
from user.models import UserProfile, RestaurantTruck, Favorite, Review, Menu

# Register your models here.

admin.site.register((
    UserProfile,
    RestaurantTruck,
    Favorite,
    Review,
    Menu
))