from rest_framework import serializers

from .models import FoodDetail, FoodType, Made_of_food, Comment

class FoodDetailSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=FoodDetail
        fields='__all__'
        
        
        
class FoodTypeSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=FoodType
        fields='__all__'        
        
        
        
class Made_of_FoodSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Made_of_food
        fields='__all__'        
        
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Comment
        fields='__all__'        