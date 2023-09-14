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
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', renderIndex.as_view(), name='home'),
    path('pricing/', renderPricing, name='pricing'),
    path('contactus/', renderContact, name='contact'),
    path('user-account/', renderAccount, name='account'),
    path('all-recipes/', renderRecipe.as_view(), name='all_recipes'),
    path('recipes-creation/', renderRecipeCreation.as_view(), name='recipe_creation'),
    path('recipes-edit/', renderRecipeEdit, name='recipe_edit'),
    path('my-recipes/', renderMyRecipes.as_view(), name='my_recipes'),
    path('recipes/<int:pk>/', renderRecipePage.as_view(), name='recipe_page'),
    path('accounts/', include('allauth.urls'), name='accounts_urls'),
]