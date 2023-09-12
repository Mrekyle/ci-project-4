from django import forms 
from .models import Recipes 

class createRecipe(forms.ModelForm):

    class Meta:
        model = Recipes
        fields = ('title',  'author', 'slug', 'recipe_desc', 'recipe_story', 'ingredients_list', 'methods_list', 'featured_image')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'recipe-title'}),
            'author': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'author_id', 'value': ''}),
            'slug': forms.TextInput(attrs={'value': '', 'placeholder': 'Please add a unique name here.'}),
            'recipe_desc': forms.Textarea(attrs={'class': 'form-control'}),
            'recipe_story': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredients_list': forms.Textarea(attrs={'class': 'form-control'}),
            'methods_list': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'})
        }

    
