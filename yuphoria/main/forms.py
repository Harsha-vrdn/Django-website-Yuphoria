# morsecode/forms.py
from django import forms

class MorseCodeForm(forms.Form):
    text_input = forms.CharField(label='Enter text', max_length=100)
