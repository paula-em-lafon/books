from django.core.validators import RegexValidator
from django.db import models
from books.autores.models import Autores
from books.editoriales.models import Editoriales


# Create your models here.
class Libros(models.Model):

	isbn = models.fields.CharField(
		max_length=13,
		validators=[RegexValidator(regex='^.{13}$', message=u'El largo debe ser de 13', code='nomatch'),
					RegexValidator(regex='^[0-9]+$', message=u'Un ISBN solo debe contener numeros', code='nomatch')],
		primary_key=True
	)
	titulo = models.fields.CharField(
		max_length=45,
		null=False
	)
	sinopsis = models.fields.TextField(
	)
	n_paginas = models.fields.CharField(
		max_length=45,
		validators=[RegexValidator(regex='^[0-9]+$', message=u'Un ISBN solo debe contener numeros', code='nomatch')]
	)
	editorial=models.ForeignKey(
		Editoriales
	)

	def __unicode__(self):
		return self.titulo

class AutoresHasLibros(models.Model):
	libros_isbn = models.ForeignKey(
		Libros,
		null=False,
		on_delete=models.CASCADE
	)
	Autores_id = models.ForeignKey(
		Autores,
		null=False,
		on_delete=models.CASCADE
	)
