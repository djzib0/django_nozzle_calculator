from django import forms

from .models import Nozzle

class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
        fields = [__all__]
        labels = {'diameter': 'średnica'}


