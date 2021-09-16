from django.db import models
from .product import Product
from .customer import Customer
import datetime
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    # first_name=models.CharField(max_length=50,default="",blank=True)
    # last_name=models.CharField(max_length=50,default="")
    # email=models.EmailField () 
    date=models.DateField(default=datetime.datetime.today())

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False