# Generated by Django 3.2 on 2023-09-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktake', '0005_recipes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]
