from django import forms
from .models import Autores

class AutorForm(forms.ModelForm):
	class Meta:
		model= Autores
		fields= ['nombre', 'apellidos']
