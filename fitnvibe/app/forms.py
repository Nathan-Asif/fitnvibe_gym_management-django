from django import forms
from .models import MembershipPlan

class MembershipPlanForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = '__all__'
        widgets = {
            'icon_color': forms.TextInput(attrs={'type': 'color'}),
        }