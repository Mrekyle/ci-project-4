from django.shortcuts import render
from django.views import generic
from .models import Recipes
from .forms import createRecipe
from django.urls import reverse, reverse_lazy

# Create your views here.

"""
Simple return render requests for templates/pages that dont need any 
other logic for them to be used by the application or user.
"""

def renderContact(request):
    return render(request, 'contactus.html', {})

def renderLogin(request):
    return render(request, 'login.html', {})

def renderPricing(request):
    return render(request, 'pricing.html', {})

def renderAccount(request):
    return render(request, 'useraccount.html', {})

"""
Class based views that contain more logic that is 
required from the database.
"""

class renderRecipeCreation(generic.CreateView):

    model = Recipes
    form_class = createRecipe
    template_name = 'recipe_create.html'

class renderIndex(generic.ListView):
    
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class renderRecipe(generic.ListView):
    
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe.html'
    paginate_by = 6

class renderRecipePage(generic.DetailView):
    
    model = Recipes
    template_name = 'recipe_page.html'

class renderMyRecipes(generic.ListView):
    
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'my_recipes.html'
    paginate_by = 9 


class renderRecipeEdit(generic.UpdateView):

    model = Recipes
    template_name = 'recipe_edit.html'
    form_class = createRecipe

class renderRecipeDelete(generic.DeleteView):

    model = Recipes
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('my_recipes')



    