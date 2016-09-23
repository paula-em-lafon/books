from django import forms
from betterforms import multiform
from collections import OrderedDict
from books.catalogue.models import Autores, Libros, Editoriales

class AutorForm(forms.ModelForm):
	class Meta:
		model= Autores
		fields= ['nombre', 'apellidos']

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libros
		fields = ('isbn', 'titulo','sinopsis', 'n_paginas', 'editorial')

class CheckedLibrosForm(forms.Form):
    # This might be better as a ModelChoiecField
    ids = forms.MultipleChoiceField()#

    def __init__(self, libros_id, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['ids'].choices = libros_id

class EditorialForm(forms.ModelForm):
	class Meta:
		model= Editoriales
		fields= ['nombre', 'sede']

class ExistingAutorForm(forms.Form):
	autores = forms.ModelMultipleChoiceField(queryset=Autores.objects.all().order_by('apellidos'))

class LibroMultiForm(multiform.MultiForm):
	form_classes = OrderedDict((
		('libro', LibroForm),
		('autor', ExistingAutorForm),
	))

