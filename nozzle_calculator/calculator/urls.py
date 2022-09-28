from django.urls import path
from .views import *

app_name = 'calculator'

urlpatterns = [
    path('', index_view, name='index'),
    path('nozzles/', nozzles_view, name='nozzles'),
    path('nozzle/<int:nozzle_id>/', nozzle_details_view, name='nozzle_details'),
    path('nozzle/<int:nozzle_id>/orders', nozzle_orders_view, name='nozzle_orders'),
    path('nozzle/<int:nozzle_id>/offers', nozzle_offers_view, name='nozzle_offers'),
    path('nozzle/<int:nozzle_id>/add_order', add_nozzle_order, name='add_nozzle_order'),
    path('nozzle/<int:nozzle_id>/order/edit_order/<int:order_id>', edit_nozzle_order, name='edit_nozzle_order'),
    path('nozzle/<int:nozzle_id>/add_offer', add_nozzle_offer, name='add_nozzle_offer'),
    path('nozzle/<int:nozzle_id>/offer/edit_offer/<int:offer_id>', edit_nozzle_offer, name='edit_nozzle_offer'),
    path('nozzle/<int:nozzle_id>/edit_nozzle', edit_nozzle, name='edit_nozzle'),
    path('nozzle/add_nozzle/', add_nozzle, name='add_nozzle'),

    path('orders/', orders_view, name='orders_view'),
]