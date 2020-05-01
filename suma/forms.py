from django import forms

class PlusForm(forms.Form):
    s1 = forms.CharField(label='Sumando uno')
    s2 = forms.CharField(label='Sumando dos')
