from django.contrib import admin

# Register your models here.
from .models import Customer, Equipment, Renter, Driver, Order, Contract

admin.site.register(Customer)
admin.site.register(Equipment)
admin.site.register(Renter)
admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(Contract)
