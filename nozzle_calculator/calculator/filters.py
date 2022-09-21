import django_filters
from django import forms

from .models import *


class NozzleFilter(django_filters.FilterSet):
    PROFILES = (('Optima', 'Optima'),
                ('19A', '19A'),
                )

    INNER_RING_TYPES = (('Complete st. st. inside', 'Wnętrze nierdzewne'),
                        ('St. st. ring inside', 'Pierścień kawitacyjny nierdzewny'),
                        ('Complete steel', 'Wnętrze ze stali zwykłej'),
                        ('St. st. ring and outlet', 'Pierścień kawitacyjny i wylot ze stali nierdzewnej'))

    YES_NO_CHOICES = (('True', 'Tak'),
                      ('False', 'Nie')
                      )

    diameter = django_filters.CharFilter(lookup_expr='icontains')
    profile = django_filters.ChoiceFilter(label="test label",
                                          choices=PROFILES,
                                          widget=forms.Select(attrs={"class": "wide_form"}))
    inner_ring_type = django_filters.ChoiceFilter(label="test label",
                                                  choices=INNER_RING_TYPES,
                                                  widget=forms.Select(attrs={"class": "wide_form"}))
    has_headbox = django_filters.ChoiceFilter(choices=YES_NO_CHOICES,
                                              widget=forms.Select(attrs={"class": "wide_form"}))
    has_outlet_ring = django_filters.ChoiceFilter(choices=YES_NO_CHOICES,
                                                  widget=forms.Select(attrs={"class": "wide_form"}))

    class Meta:
        model = Nozzle
        fields = '__all__'
        exclude = ['date_created']

    # below code to not show any results after loading page.
    # it will show result of filtering after pressing search button.
    def __init__(self, *args, **kwargs):
        super(NozzleFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class OrderFilter(django_filters.FilterSet):
    order_dmcg_number = django_filters.CharFilter(lookup_expr='icontains')
    order_client_number = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_created', 'nozzle']
