from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='test')    
    bio = models.TextField(default='')

    def __string__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __string__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50, default='2')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __string__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
        )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} in {self.recipe.name}"