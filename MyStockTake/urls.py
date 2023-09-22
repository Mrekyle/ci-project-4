from django.contrib import admin
from django.urls import path, include

from stocktake.views import (
    renderContact,
    renderIndex,
    renderPricing,
    renderAccount,
    renderRecipe,
    renderRecipePage,
    renderRecipeCreation,
    renderMyRecipes,
    renderRecipeEdit,
    renderRecipeDelete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', renderIndex.as_view(), name='home'),
    path('pricing/', renderPricing, name='pricing'),
    path('contactus/', renderContact, name='contact'),
    path('user-account/', renderAccount, name='account'),
    path('all-recipes/',
         renderRecipe.as_view(), name='all_recipes'),
    path('recipes/<int:pk>/',
         renderRecipePage.as_view(), name='recipe_page'),
    path('my-recipes/',
         renderMyRecipes.as_view(), name='my_recipes'),
    path('recipes-creation/',
         renderRecipeCreation.as_view(),
         name='recipe_creation'),
    path('my-recipes/<int:pk>/edit',
         renderRecipeEdit.as_view(),
         name='recipe_edit'),
    path('my-recipes/<int:pk>/delete',
         renderRecipeDelete.as_view(), name='delete_recipe'),
    path('accounts/',
         include('allauth.urls'), name='accounts_urls'),
]
