from django import forms

class AddingForm(forms.Form):
    s1 = forms.CharField(label='Sumando uno')
    s2 = forms.CharField(label='Sumando dos')
