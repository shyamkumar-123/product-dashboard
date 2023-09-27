from django.db import models
class Product(models.Model):
    #changing the value  (1 or 2 or 3) to mobile or cloths or shoes for knowing the categories to the user.
    CAT=(('1','Mobile'),('2','Cloths'),('3','shoes'))
    STATUS=(('1','Active'),('0','Inactive')) #For understainding of the user if the status is active or not.
    name=models.CharField(max_length=50,verbose_name="product Name")
    cat=models.CharField(max_length=50,verbose_name="category",choices=CAT)
    price=models.FloatField(verbose_name="Product price")
    status=models.CharField(max_length=50,verbose_name="product status",choices=STATUS)
    uid=models.IntegerField()

    def __str__(self):
        return self.name
    

