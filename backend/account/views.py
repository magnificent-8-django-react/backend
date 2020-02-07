from django.shortcuts import render
from account.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer

# class ModelView(viewsets.ModelViewSet):
#     queryset = Class.objects.all()
#     # serializer_class = AccountSerializer

#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]
#     serializer_class = AccountSerializer

#     def get_queryset(self):
#         return self.request.user.holder.all()

#     def perform_create(self, serializer):
#         serializer.save(holder=self.request.user)