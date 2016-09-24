from django import forms
from betterforms import multiform
from collections import OrderedDict
from books.autores.models import Autores

from .models import Libros

class ExistingAutorForm(forms.Form):
	autores = forms.ModelMultipleChoiceField(queryset=Autores.objects.all().order_by('apellidos'))

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libros
		fields = ('isbn', 'titulo','sinopsis', 'n_paginas', 'editorial')

class LibroMultiForm(multiform.MultiForm):
	form_classes = OrderedDict((
		('libro', LibroForm),
		('autor', ExistingAutorForm),
	))