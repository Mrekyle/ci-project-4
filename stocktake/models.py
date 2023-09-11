from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Published'))

class Recipes(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_post')
    recipe_desc = models.CharField(max_length=150, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    ingredients_list = models.TextField(blank=True)
    methods_list = models.TextField(blank=True)
    recipe_story = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'