from django import forms

from .models import Nozzle, Order

class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
        fields = '__all__'
        labels = {'diameter': 'Średnica'}


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {'order_client_number', 'order_dmcg_number',}
        labels = {'order_dmcg_number': 'Numer zlecenia DMCG',
                  'order_client_number': 'Numer zlecenia klienta'}
        widgets = {
            'order_dmcg_number': forms.TextInput(attrs={
                'class': "form_control",
                'style': 'width: 12em;',
                'placeholder': 'Numer DMCG'
            })
        }




