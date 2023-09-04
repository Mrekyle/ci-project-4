from ..templates import views 
from django.urls import path

urlPatterns = [
    path('', views.renderIndex, name='home'),
    path('/pricing/', views.renderPricing, name='pricing'),
    path('/contact/', views.renderContact, name='contact'),
    path('/user-account/', views.renderAccount, name='account'),
    path('/recipes/', views.renderRecipe, name='recipes'),
]