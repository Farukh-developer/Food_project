from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FoodType(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Made_of_food(models.Model):
    made=models.CharField(max_length=30)
    def __str__(self):
        return self.made
    
    

class FoodDetail(models.Model):
    foodtype=models.ForeignKey(FoodType, on_delete=models.CASCADE)
    made_of_food=models.ForeignKey(Made_of_food, on_delete=models.CASCADE)
    price=models.IntegerField()
    
    


class Comment(models.Model):
    text=models.CharField(max_length=200)
    ranking_of_food=models.CharField(max_length=20)
    author=models.ForeignKey(User, on_delete=models.CASCADE) 
    created=models.DateTimeField(auto_now_add=True)