from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User  # Import User model
from .models import Recipe, RecipeIngredient, Ingredient, Profile

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine,]

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    in_lines = [RecipeIngredientInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)





