from django import forms

from .models import Nozzle, Order

class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
        fields = '__all__'
        labels = {'diameter': 'średnica'}


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {'order_dmcg_number': 'Numer zlecenia DMCG',
                  'order_client_number': 'Numer zlecenia klienta'}



