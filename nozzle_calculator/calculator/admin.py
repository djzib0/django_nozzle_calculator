from django.contrib import admin
from .models import Nozzle, Order, Offer, NozzleCalculation, AdditionalHours

# Register your models here.
admin.site.register(Nozzle)
admin.site.register(Order)
admin.site.register(Offer)
admin.site.register(NozzleCalculation)
admin.site.register(AdditionalHours)


