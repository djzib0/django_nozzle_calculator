from django.urls import path
from .views import *

app_name = 'calculator'

urlpatterns = [
    path('', index_view, name='index'),
    path('nozzles/', nozzles_view, name='nozzles'),
    path('nozzles/<int:nozzle_id>/', nozzle_details_view, name='nozzle_details'),
    path('nozzle/<int:nozzle_id>/orders', nozzle_orders_view, name='nozzle_orders'),
]