from . import views 
from django.urls import path

urlPatterns = [
    path('', views.home, name='home'),
    path('/pricing/', views.renderPricing, name='pricing'),
]