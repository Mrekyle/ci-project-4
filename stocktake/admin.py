from django.contrib import admin
from .models import Recipes, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Recipes)
class AdminRecipe(SummernoteModelAdmin):

    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'author', 'created_on']
    summernote_fields = ('recipe_desc'), ('ingredients_list'), ('methods_list'), ('recipe_story')

@admin.register(Comment)
class AdminComment(SummernoteModelAdmin):

    list_display = ('name', 'email', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email', 'created_on')