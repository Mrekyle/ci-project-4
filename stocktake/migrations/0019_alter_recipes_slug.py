# Generated by Django 3.2 on 2023-09-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktake', '0018_auto_20230911_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='slug',
            field=models.SlugField(max_length=30, null=True, unique=True),
        ),
    ]