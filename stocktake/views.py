from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipes

# Create your views here.

def renderIndex(request):
    return render(request, 'index.html', {})

def renderContact(request):
    return render(request, 'contactus.html', {})

def renderLogin(request):
    return render(request, 'login.html', {})

def renderPricing(request):
    return render(request, 'pricing.html', {})

def renderAccount(request):
    return render(request, 'useraccount.html', {})

def renderRecipeCreation(request):
    
    if request.method == 'POST':
            title = request.POST.get('title')
            recipe_desc = request.POST.get('recipe_desc')
            recipe_story = request.POST.get('recipe_story')
            ingredients_list = request.POST.get('ingredients_list')
            methods_list = request.POST.get('method_list')
            # img_upload = request.POST.get('image-upload')

            Recipes.objects.create(title=title, recipe_desc=recipe_desc, recipe_story=recipe_story, ingredients_list=ingredients_list, methods_list=methods_list)
            
            return redirect('recipe.html')
    
    if request.method == 'GET':
        return render(request, 'recipe_create.html', {})

def renderRecipeEdit(request):
    return render(request, 'recipe_edit.html', {})

def renderMyRecipes(request):
    return render(request, 'my_recipes.html', {})

class renderRecipe(generic.ListView):
    
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe.html'
    paginate_by = 6

class renderRecipePage(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipes.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            'recipe_page.html', 
            {
                'recipe': recipe,
                'comments': comments,
                'liked': liked,
            },
        )
    
# class renderRecipeCreation(View):

#     def get(self, request):
#         return render(request, 'recipE_create.html')
    
#     def post(self, request):
#         if request.method == 'POST':
#             title = request.POST.get('title')
#             description = request.POST.get('description')
#             story = request.POST.get('story')
#             ingredients = request.POST.get('ingredients')
#             method = request.POST.get('method')
#             img_upload = request.POST.get('image-upload')

#             Recipes.objects.create(title=title, description=description, 
#                                    story=story, ingredients=ingredients, method=method)
            
#             return redirect('renderRecipePage')
      