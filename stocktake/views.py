from django.shortcuts import render

# Create your views here.

def renderBase(request):
    return render(request, 'base.html', {})

def renderIndex(request):
    return render(request, 'index.html', {})

def renderContact(request):
    return render(request, 'contactus.html', {})

def renderLogin(request):
    return render(request, 'login.html', {})

def renderPricing(request):
    return render(request, 'pricing.html', {})
