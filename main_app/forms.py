from django.forms import ModelForm
from .models import Hire

class HireForm(ModelForm):
    class Meta:
        model = Hire
        fields = ['date', 'event']
