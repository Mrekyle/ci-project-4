from . import views
from django.urls import path

urlPatterns = [
    path('', views.renderIndex.as_view(), name='home'),
    path('/pricing/', views.renderPricing, name='pricing'),
    path('/contact/', views.renderContact, name='contact'),
    path('/user-account/', views.renderAccount, name='account'),
    path('/all-recipes/', views.renderRecipe.as_view(), name='all_recipes'),
    path('/recipes/<int:pk>/',
         views.renderRecipePage.as_view(), name='recipe_page'),
    path('/my-recipes/', views.renderMyRecipes.as_view(), name='my_recipes'),
    path('/recipes-creation/', views.renderRecipeCreation.as_view(),
         name='recipe_creation'),
    path('/my-recipes/<int:pk>/edit',
         views.renderRecipeEdit.as_view(), name='recipe_edit'),
    path('/my-recipes/<int:pk>/delete',
         views.renderRecipeDelete.as_view(), name='delete_recipe'),
]
