from django.shortcuts import render
from user.models import RestaurantTruck, Review, Menu
from rest_framework import viewsets, permissions
from restaurant.serializers import RestaurantTruckSerializer, ReviewSerializer, MenuSerializer

class RestaurantTruckViewSet(viewsets.ModelViewSet):
    queryset = RestaurantTruck.objects.all().order_by('id')
    serializer_class = RestaurantTruckSerializer

    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # serializer_class = BranchSerializer

    # def get_queryset(self):
    #     return self.request.user.owner.all()
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
