from django.test import TestCase
from books.catalogue.forms import LibroForm, AutorForm, EditorialForm


class FormTests(TestCase):
	def test_libro_form(self):
		form_data={
			'isbn': '1234567890123',
			'titulo': 'algo',
			'sinopsis': 'algo mas largo',
			'n_paginas': '13',
			'editorial' : ''
		}
		form = LibroForm(data=form_data)
		self.assertTrue(form.is_valid())

	def test_autor_form(self):
		form_data={
			'nombre': 'Juanito',
			'apellidos': 'Perez',
		}
		form = AutorForm(data=form_data)
		self.assertTrue(form.is_valid())

	def test_editorial_form(self):
		form_data={
			'nombre': 'Chuy y asosiados',
			'sede': 'Chihuahua',
		}
		form = EditorialForm(data=form_data)
		self.assertTrue(form.is_valid())
