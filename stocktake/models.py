from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from ckeditor.fields import RichTextField

STATUS = ((0, 'Draft'), (1, 'Published'))

class Recipes(models.Model):
    """
    The main recipe model to build the database. Which is then split
    out to each page that renders the recipe.
    """
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_post')
    recipe_desc = models.CharField(max_length=150, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    ingredients_list = RichTextField(blank=True, null=True)
    methods_list = RichTextField(blank=True, null=True)
    recipe_story = RichTextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')