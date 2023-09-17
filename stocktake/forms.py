from django import forms 
from .models import Recipes 

class createRecipe(forms.ModelForm):

    class Meta:
        model = Recipes
        fields = ('title',  'author', 'recipe_desc', 'recipe_story', 'ingredients_list', 'methods_list', 'featured_image')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'recipe-title form4Example3', 'rows': '4'}),
            'author': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'author_id', 'value': ''}),
            'recipe_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_story': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredients_list': forms.Textarea(attrs={'class': 'form-control'}),
            'methods_list': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'})
        }

    
