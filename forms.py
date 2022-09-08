from turtle import color
from django import forms

class RemerasFormulario(forms.Form):
    color = forms.CharField(max_length=50)
    talle = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)

class PantalonesFormulario(forms.Form):   
    color = forms.CharField(max_length=50)
    talle = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)

class CalzadoFormulario(forms.Form):   
    color = forms.CharField(max_length=50)
    talle = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
