from . import views 
from django.urls import path

urlPatterns = [
    path('', views.renderIndex, name='home'),
    path('/pricing/', views.renderPricing, name='pricing'),
]