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

def renderRecipe(request):
    return render(request, 'recipe.html', {})