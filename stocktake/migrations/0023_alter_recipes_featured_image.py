# Generated by Django 3.2 on 2023-09-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktake', '0022_auto_20230919_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='featured_image',
            field=models.ImageField(default='placeholder', upload_to='media/', verbose_name='image'),
        ),
    ]