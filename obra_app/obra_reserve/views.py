from django.shortcuts import render
import hashlib, binascii
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from obra_reserve.models import Customer, Driver, Renter, Equipment, Order, Contract
from obra_reserve.serializers import CustomerSerializer, EquipmentSerializer, RenterSerializer, DriverSerializer, OrderSerializer, ContractSerializer

# Import csrf to allow other domains to access our API menthods
# Json parser parses incoming data into data model
# Import all models from your ReservationApp.models along with corresponding
# Serializer classes
# Create your views here.

@csrf_exempt
def customerApi(request, id=0):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customers_serializer = CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Customer Created Successfully", safe=False)
        else:return JsonResponse("Failed to Add Customer",safe=False)
    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer = Customer.objects.get(
            id=customer_data['id'])
        customers_serializer = CustomerSerializer(customer, data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Customer Updated Successfully", safe=False)
        else:return JsonResponse("Failed to Update Customer",safe=False)
    elif request.method == 'DELETE':
        customer=Customer.objects.get(id=id)
        customer.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def customer_index_Api(request, id=int):
    if request.method == 'GET':
        customer = Customer.objects.get(id=id)
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data, safe=False)

@csrf_exempt
def scramble(password: str):
    password = hashlib.pbkdf2_hmac(b'password',b'salt','10000')
    binascii.hexlify(password)

@csrf_exempt
def equipmentApi(request, id=id):
    if request.method == 'GET':
        equipments = Equipment.objects.all()
        equipments_serializer = EquipmentSerializer(equipments, many=True)
        return JsonResponse(equipments_serializer.data, safe=False)
    elif request.method == 'POST':
        equipment_data = JSONParser().parse(request)
        equipments_serializer = EquipmentSerializer(data=equipment_data)
        if equipments_serializer.is_valid():
            equipments_serializer.save()
            return JsonResponse("Equipment Added Successfully")
        else:return JsonResponse("Failed to Add Equipment", safe=False)
    elif request.method == 'PUT':
        equipment_data = JSONParser().parse(request)
        equipment = Equipment.objects.get(id=equipment_data['id'])
        equipments_serializer = EquipmentSerializer(equipment, data=equipment_data)
        if equipments_serializer.is_valid():
            equipments_serializer.save()
            return JsonResponse("Equipment Updated Successfully", safe=False)
        else:return JsonResponse("Failed to Update Equipment", safe=False)
    elif request.method == 'DELETE':
        equipment = Equipment.objects.get(id=id)
        equipment.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def equipment_index_Api(request, id=int):
    if request.method == 'GET':
        equipment = Equipment.objects.get(id=id)
        equipment_serializer = EquipmentSerializer(equipment)
        return JsonResponse(equipment_serializer.data, safe=False)

@csrf_exempt
def renterApi(request, id=0):
    if request.method == 'GET':
        renters = Renter.objects.all()
        renters_serializer = RenterSerializer(renters, many=True)
        return JsonResponse(renters_serializer.data, safe=False)
    elif request.method == 'POST':
        renter_data = JSONParser().parse(request)
        renters_serializer = RenterSerializer(data=renter_data)
        if renters_serializer.is_valid():
            renters_serializer.save()
            return JsonResponse("Renter Created Successfully", safe=False)
        else:return JsonResponse("Failed to Add Renter",safe=False)
    elif request.method == 'PUT':
        renter_data = JSONParser().parse(request)
        renter = Renter.objects.get(
            id=renter_data['id'])
        renters_serializer = RenterSerializer(renter, data=renter_data)
        if renters_serializer.is_valid():
            renters_serializer.save()
            return JsonResponse("Renter Updated Successfully", safe=False)
        else:return JsonResponse("Failed to Update Renter",safe=False)
    elif request.method == 'DELETE':
        renter=Renter.objects.get(id=id)
        renter.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def renter_index_Api(request, id=int):
    if request.method == 'GET':
        renter = Renter.objects.get(id=id)
        renter_serializer = RenterSerializer(renter)
        return JsonResponse(renter_serializer.data, safe=False)

@csrf_exempt
def scramble(password: str):
    password = hashlib.pbkdf2_hmac(b'password',b'salt','10000')
    binascii.hexlify(password)

@csrf_exempt
def driverApi(request, id=0):
    if request.method == 'GET':
        drivers = Driver.objects.all()
        drivers_serializer = DriverSerializer(drivers, many=True)
        return JsonResponse(drivers_serializer.data, safe=False)
    elif request.method == 'POST':
        driver_data = JSONParser().parse(request)
        drivers_serializer = DriverSerializer(data=driver_data)
        if drivers_serializer.is_valid():
            drivers_serializer.save()
            return JsonResponse("Driver Registered Successfully")
        return JsonResponse("Failed to Register Driver", safe=False)
    elif request.method == 'PUT':
        driver_data = JSONParser().parse(request)
        driver = Driver.objects.get(id=driver_data['id'])
        drivers_serializer = DriverSerializer(driver, data=driver_data)
        if drivers_serializer.is_valid():
            drivers_serializer.save()
            return JsonResponse("Driver Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Driver")
    elif request.method == 'DELETE':
        driver = Driver.objects.get(id=id)
        driver.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def driver_index_Api(request, id=int):
    if request.method == 'GET':
        driver = Driver.objects.get(id=id)
        driver_serializer = DriverSerializer(driver)
        return JsonResponse(driver_serializer.data, safe=False)

@csrf_exempt
def scramble(password: str):
    password = hashlib.pbkdf2_hmac(b'password',b'salt','10000')
    binascii.hexlify(password)

@csrf_exempt
def orderApi(request, id=0):
    if request.method == 'GET':
        orders = Order.objects.all()
        orders_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        orders_serializer = OrderSerializer(data=order_data)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse("Order Created Successfully")
        return JsonResponse("Failed to Create Order", safe=False)
    elif request.method == 'PUT':
        order_data = JSONParser().parse(request)
        order = Order.objects.get(id=order_data['id'])
        orders_serializer = OrderSerializer(order, data=order_data)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse("Order Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Order")
    elif request.method == 'DELETE':
        order = Order.objects.get(id=id)
        order.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def order_index_Api(request, id=int):
    if request.method == 'GET':
        order = Order.objects.get(id=id)
        order_serializer = OrderSerializer(order)
        return JsonResponse(order_serializer.data, safe=False)

@csrf_exempt
def contractApi(request, id=0):
    if request.method == 'GET':
        contracts = Contract.objects.all()
        contracts_serializer = ContractSerializer(contracts, many=True)
        return JsonResponse(contracts_serializer.data, safe=False)
    elif request.method == 'POST':
        contract_data = JSONParser().parse(request)
        contracts_serializer = ContractSerializer(data=contract_data)
        if contracts_serializer.is_valid():
            contracts_serializer.save()
            return JsonResponse("Contract Created Successfully")
        return JsonResponse("Failed to Create Contract", safe=False)
    elif request.method == 'PUT':
        contract_data = JSONParser().parse(request)
        contract = Order.objects.get(id=contract_data['id'])
        contract_serializer = ContractSerializer(contract, data=contract_data)
        if contract_serializer.is_valid():
            contract_serializer.save()
            return JsonResponse("Contract Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Contract")
    elif request.method == 'DELETE':
        contract = Contract.objects.get(id=id)
        contract.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def contract_index_Api(request, id=int):
    if request.method == 'GET':
        contract = Contract.objects.get(id=id)
        contract_serializer = ContractSerializer(contract)
        return JsonResponse(contract_serializer.data, safe=False)







