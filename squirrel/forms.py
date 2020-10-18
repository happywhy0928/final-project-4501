from django.forms import ModelForm
from .models import Squirrel


class CreateNewSighting(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

class UpdateSighting(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
            'latitude',
            'longitude',
            'unique_id',
            'shift',
            'date',
            'age',
            'furColor',
            'running',
            'eating',
            'climbing',
        ]
