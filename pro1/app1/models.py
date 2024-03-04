from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=70)
    product_category = models.CharField(max_length=40)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_expiry_date = models.DateField(blank=True, null=True)
    product_manufacturing_date = models.DateField()
    product_HSN_no = models.CharField(max_length=20)
    product_quantity = models.IntegerField()