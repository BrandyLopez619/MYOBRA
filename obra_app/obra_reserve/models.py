from django.db import models
#from django.contrib.auth.hashers import make_password
#Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    contact_number = models.CharField(unique=True, max_length=16)
    credit_card = models.CharField(unique=True, max_length=20)
    billing_address = models.CharField(unique=True, max_length=50)
    password = models.CharField(null=False, max_length=17)
    registered = models.DateTimeField(auto_now_add=True)

"""    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Customer, self).save(*args, **kwargs)"""

class Renter(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    contact_number = models.CharField(unique=True, max_length=16)
    credit_card = models.CharField(unique=True, max_length=20)
    billing_address = models.CharField(unique=True, max_length=50)
    password = models.CharField(null=False, max_length=17)
    registered = models.DateTimeField(auto_now_add=True)

"""    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Renter, self).save(*args, **kwargs)
"""
class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    contact_number = models.CharField(unique=True, max_length=16)
    credit_card = models.CharField(unique=True, max_length=20)
    billing_address = models.CharField(unique=True, max_length=50)
    vin_number = models.CharField(max_length=20, default=None)
    available = models.CharField(null=False, max_length=20)
    password = models.CharField(null=False, max_length=17)
    registered = models.DateTimeField(auto_now_add=True)

"""    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Driver, self).save(*args, **kwargs)
"""
class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(null=False, max_length=4)
    brand_name = models.CharField(null=False, max_length=20)
    model_name = models.CharField(null=False, max_length=20)
    serial_number = models.CharField(unique=True, null=False, max_length=20)
    current_location = models.CharField(max_length=50)
    daily_rate = models.CharField(null=False, max_length=20)
    available = models.CharField(null=False, max_length=20)
    registered = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    ordered = models.DateTimeField(auto_now_add=True)
    delivery_location = models.CharField(max_length=64)
    delivery_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=100)



class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    delivery_location = models.CharField(max_length=64)
    delivery_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

