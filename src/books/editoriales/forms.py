from django import forms

from .models import Editoriales

class EditorialForm(forms.ModelForm):
	class Meta:
		model= Editoriales
		fields= ['nombre', 'sede']
