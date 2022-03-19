from django.urls import path
from obra_reserve import views

urlpatterns = [
    
    path(r'customer',views.customerApi),
    path(r'customer/<int:id>/',views.customer_index_Api),
    
    path(r'equipment',views.equipmentApi),
    path(r'equipment/<int:id>/',views.equipment_index_Api),

    path(r'renter',views.renterApi),
    path(r'renter/<int:id>/',views.renter_index_Api),

    path(r'driver',views.driverApi),
    path(r'driver/<int:id>/)',views.driver_index_Api),

    path(r'order',views.orderApi),
    path(r'order/<int:id>/',views.order_index_Api),

    path(r'contract',views.contractApi),
    path(r'contract/<int:id>/',views.contract_index_Api)
]

