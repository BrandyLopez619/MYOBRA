from rest_framework import serializers
from obra_reserve.models import Customer, Equipment, Renter, Driver, Order, Contract 
from hashlib import pbkdf2_hmac
#Serializers basically help convert complex types or model instances into native 
#python datatypes that can then be easily rendered into Json XML or other content types.
#They also help with serialization which is simply reverting data back into complex types

def hash_password(password):
    dk = pbkdf2_hmac('sha256', b'password', b'bad salt'*2, 5000)
    return dk.hex()

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email',
                  'contact_number', 'credit_card', 'billing_address', 'password')

        Customer.password = hash_password(Customer.password)  # hash algorythm working (insomia: reads encryption, sql: will not apply encryption)

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'year', 'brand_name', 'model_name', 'serial_number',
                  'current_location', 'daily_rate', 'available')

class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renter
        fields = ('id', 'first_name', 'last_name', 'email',
                  'contact_number', 'credit_card', 'billing_address','password')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'first_name', 'last_name', 'email',
                  'contact_number', 'credit_card', 'billing_address','password',
                  'vin_number', 'available')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'equipment', 'ordered',
                  'delivery_location', 'delivery_mm_dd_yy')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'driver', 'customer', 'equipment', 'ordered',
                  'delivery_location', 'delivery_mm_dd_yy')

