import django_filters
from django import forms

from .models import *

class NozzleFilter(django_filters.FilterSet):
    INNER_RING_TYPES = (('Complete st. st. inside', 'Complete st. st. inside'),
                        ('St. st. ring inside', 'St. st. ring inside'),
                        ('Complete steel', 'Complete steel'),
                        ('St. st. ring and outlet', 'St. st. ring and outlet'))

    diameter = django_filters.CharFilter(widget=forms.TextInput(attrs={"class":"wide_form"}))
    inner_ring_type = django_filters.ChoiceFilter(label="test label", choices=INNER_RING_TYPES, widget=forms.Select(attrs={"class":"wide_form"}))

    class Meta:
        model = Nozzle
        fields = '__all__'
        exclude = ['date_created']


class OrderFilter(django_filters.FilterSet):
    order_dmcg_number = django_filters.CharFilter(lookup_expr='icontains')
    order_client_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_created', 'nozzle']