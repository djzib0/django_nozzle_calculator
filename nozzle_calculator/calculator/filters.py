import django_filters

from .models import *

class NozzleFilter(django_filters.FilterSet):
    class Meta:
        model = Nozzle
        fields = '__all__'
        exclude = ['date_created']