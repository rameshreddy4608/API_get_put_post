from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category_name=models.CharField(max_length=100)
    category_id=models.IntegerField(primary_key=True)
    
    def __str__(self) -> str:
        return self.category_name
    
class Product(models.Model):
    category_name=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    Pname=models.CharField(max_length=100)
    Pid=models.PositiveIntegerField(primary_key=True)
    Price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()
    
    def __str__(self) -> str:
        return self.Pname 