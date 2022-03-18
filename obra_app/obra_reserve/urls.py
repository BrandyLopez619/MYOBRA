from django.urls import path
from obra_reserve import views

urlpatterns = [
    
    path(r'customer',views.customerApi),
    path(r'customer/([0-9]+)',views.customer_index_Api),
    
    path(r'equipment',views.equipmentApi),
    path(r'equipment/([0-9]+)',views.equipment_index_Api),

    path(r'renter',views.renterApi),
    path(r'renter/([0-9]+)',views.renter_index_Api),

    path(r'driver',views.driverApi),
    path(r'driver/([0-9]+))',views.driver_index_Api),

    path(r'order',views.orderApi),
    path(r'order/([0-9]+)',views.order_index_Api),

    path(r'contract',views.contractApi),
    path(r'contract/([0-9]+)',views.contract_index_Api)
]

