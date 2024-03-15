from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = 'recipe_list.html'
    redirect_field_name = 'recipes'

class recipe_detail(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id).name
        ingredients = RecipeIngredient.objects.filter(recipe__name = recipe)
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
        }
        return render(request, 'recipe_detail.html', context)
