from django.contrib import admin
from .models import FoodDetail, FoodType, Made_of_food, Comment
# Register your models here.
admin.site.register([ FoodDetail, FoodType, Made_of_food, Comment ])