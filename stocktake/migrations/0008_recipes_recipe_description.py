# Generated by Django 3.2 on 2023-09-05 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stocktake', '0007_remove_recipes_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='recipe_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
