from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        ingredients = RecipeIngredient.objects.filter(recipe__name=recipe.name)
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
        }
        return render(request, 'recipe_detail.html', context)
