from django import forms 
from .models import Case

class ReportCase(forms.ModelForm):
    class Meta:
        model = Case  
        fields = ['desc', 'location', 'reporter_phone'] 
        widgets = {
            'desc' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'reporter_phone' : forms.TextInput(attrs={'class':'form-control'}),
        }