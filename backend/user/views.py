from django.shortcuts import render
from user.models import UserProfile, Favorite
from rest_framework import viewsets, permissions
from user.serializers import UserProfileSerializer, FavoriteSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer

    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # serializer_class = BranchSerializer

    # def get_queryset(self):
    #     return self.request.user.owner.all()
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all().order_by('id')
    serializer_class = FavoriteSerializer