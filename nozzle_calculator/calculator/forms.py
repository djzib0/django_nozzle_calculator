from django import forms

from .models import Nozzle, Order

class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
        fields = '__all__'
        labels = {'diameter': 'Średnica',
                  'drawing_number': 'Nr rysunku',
                  'profile_height': 'Wysokość',
                  'theoretical_weight': 'Ciężar wg zapytania ofertowego',
                  'real_weight': 'Ciężar rzeczywisty',
                  'inner_ring_type': 'Pierścień wewnętrzny',
                  'inner_ring_thickness_propeller_zone': 'Grubość pierścienia kawitacyjnego',
                  'inner_ring_thickness_inlet_zone': 'Grubość wlotu',
                  'inner_ring_thickness_outlet_zone': 'Grubość wylotu',
                  'ribs_quantity': 'Ilość żeber',
                  'ribs_thickness': 'Grubość żeber',
                  'segments_quantity': 'Ilość półek',
                  'segments_thickness': 'Grubość półek',
                  'has_headbox': 'Dysza ze skrzynią?',
                  'has_outlet_ring': 'Dysza z pierścieniem wlotowym?'}


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




