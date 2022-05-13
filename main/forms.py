from django import forms 
from .models import Case
from accounts.models import Investigator

class ReportCase(forms.ModelForm):
    class Meta:
        model = Case  
        fields = ['desc', 'location', 'reporter_phone'] 
        widgets = {
            'desc' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'reporter_phone' : forms.TextInput(attrs={'class':'form-control'}),
        }

class RegisterInvestigator(forms.ModelForm):
    class Meta:
        model = Investigator  
        fields = ['name', 'phone', 'email'] 
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
        }