from django import forms
from .models import ExcessFood

class ExcessFoodForm(forms.ModelForm):
    class Meta:
        model = ExcessFood
        fields = '__all__'
        widgets = {
            'best_before': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'pickup_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
