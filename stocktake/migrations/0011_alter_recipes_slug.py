# Generated by Django 3.2 on 2023-09-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktake', '0010_remove_recipes_recipe_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='slug',
            field=models.SlugField(max_length=130, unique=True),
        ),
    ]