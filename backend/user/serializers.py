from rest_framework import serializers
from user.models import UserProfile, Favorite

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'account']

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'favorite']