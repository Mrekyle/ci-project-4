from django.shortcuts import render

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

# def renderRecipe(request):
#     return render(request, 'recipe.html', {})

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipes

class renderRecipe(generic.ListView):
    
    recipe = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe.html'
    paginate_by = 6


# class renderRecipePost(View):
    
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Recipes.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True
#         return render(
#             request,
#             'recipe.html',
#             {
#                 'post': post,
#                 'comments': comments,
#                 'commented': False,
#                 'liked': liked,
#             },
#         )