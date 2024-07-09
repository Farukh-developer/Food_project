from django.shortcuts import render
from .models import FoodDetail, FoodType, Made_of_food, Comment
from .serializers import FoodDetailSerializer, FoodTypeSerializer, Made_of_FoodSerializer, CommentSerializer
# Create your views here.
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication,BaseAuthentication, SessionAuthentication

class FoodDetailAPIView(ModelViewSet):
    queryset=FoodDetail.objects.all()
    serializer_class=FoodDetailSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
 
 
class FoodTypelAPIView(ModelViewSet):
    queryset=FoodType.objects.all()
    serializer_class=FoodTypeSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[BaseAuthentication, SessionAuthentication]
        
        
class Made_of_FoodAPIView(ModelViewSet):
    queryset=Made_of_food.objects.all()
    serializer_class=Made_of_FoodSerializer            
    
    
class CommentDetailAPIView(ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer