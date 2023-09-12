from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipes
from .forms import createRecipe

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

def renderRecipeEdit(request):
    return render(request, 'recipe_edit.html', {})

"""
Class based views that contain more logic that is 
required from the database.
"""

# def renderRecipeCreation(request):
    
#     if request.method == 'POST':
#             title = request.POST.get('title')
#             recipe_desc = request.POST.get('recipe_desc')
#             recipe_story = request.POST.get('recipe_story')
#             ingredients_list = request.POST.get('ingredients_list')
#             methods_list = request.POST.get('method_list')
#             author_id = request.POST.get('user.id')
#             # img_upload = request.POST.get('image-upload')

#             Recipes.objects.create(title=title, recipe_desc=recipe_desc, recipe_story=recipe_story, ingredients_list=ingredients_list, methods_list=methods_list, author_id=author_id)
            
#             return redirect('recipe.html')
    
#     if request.method == 'GET':
#         return render(request, 'recipe_create.html', {})

class renderRecipeCreation(generic.CreateView):

    model = Recipes
    form_class = createRecipe
    template_name = 'recipe_create.html'
    # fields = ('title', 'recipe_desc', 'slug', 'author', 'recipe_story', 'ingredients_list', 'methods_list', 'featured_image')


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

class renderMyRecipes(generic.ListView):
    
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'my_recipes.html'
    paginate_by = 9 



    