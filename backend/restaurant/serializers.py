from rest_framework import serializers
from user.models import RestaurantTruck, Review, Menu

class RestaurantTruckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantTruck
        # fields = '__all__'
        fields = ['id', 'restaurant', 'username', 'email', 'phone', 'rating', 'owner']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ['id', 'stars', 'comment', 'truck_review', 'customer_voice']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        # fields = '__all__'
        fields = ['id', 'dish', 'image', 'description', 'restaurant_name']