from django.shortcuts import render
from django.http import HttpResponseRedirect
from books.catalogue.forms import AutorForm,EditorialForm, LibroMultiForm
from books.utils.mixins.forms.multiform import MultiFormsView
from django.views.generic.edit import CreateView, FormView
from books.catalogue.models import Libros, AutoresHasLibros, Autores



class CreateAutorView(CreateView):
	form_class= AutorForm
	success_url= '/admin/'
	template_name= 'autores/create.html'

class CreateEditorialView(CreateView):
	form_class= EditorialForm
	success_url= '/admin/'
	template_name= 'autores/create.html'

class CreateLibroView(FormView):
	success_url= '/admin/'
	form_class= LibroMultiForm
	template_name= 'autores/create.html'

	def form_valid(self, form):
		#Guardar Libros
		libro_dict = form['libro'].cleaned_data
		libro =Libros(**libro_dict)
		libro.save()

		#Crear objeto autores_has_libros y asignar isbn
		autores_has_libros = AutoresHasLibros()
		autores_has_libros.libros_isbn = libro
		
		#Asigar Autor
		autor = form['autor'].cleaned_data['autores'][0]
		autores_has_libros.Autores_id = autor
		autores_has_libros.save()
_
		return HttpResponseRedirect(self.get_success_url())