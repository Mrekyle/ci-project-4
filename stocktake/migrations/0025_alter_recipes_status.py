# Generated by Django 3.2 on 2023-09-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktake', '0024_alter_recipes_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
