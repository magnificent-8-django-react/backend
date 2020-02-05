from rest_framework import serializers
from restaurant.models import RestaurantTruck, Review, Menu

class RestaurantTruckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantTruck
        fields = ['id', 'restaurant', 'username', 'email', 'phone', 'rating', 'owner']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'stars', 'comment', 'truck_review', 'customer_voice']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'dish', 'image', 'description', 'restaurant']