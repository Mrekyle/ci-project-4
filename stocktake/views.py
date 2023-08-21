from django.shortcuts import render

# Create your views here.

def render_base(request):
    return render(request, 'base.html', {})
