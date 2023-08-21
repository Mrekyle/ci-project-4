from django.db import models

# Create your models here.


class ProductCatalog(models.Model):
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    product_category = models.CharField(max_length=20)
    product_weight = models.IntegerField()
    product_price = models.IntegerField()

    