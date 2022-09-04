from django.urls import path
from .views import *

app_name = 'calculator'

urlpatterns = [
    path('', indexView, name='index'),
    path('nozzles/', nozzlesView, name='nozzles'),
    path('nozzles/<int:nozzle_id>/', nozzleDetailsView, name='nozzle_details'),
    path('nozzle/<int:nozzle_id>/orders', nozzleOrdersView, name='nozzle_orders'),
]