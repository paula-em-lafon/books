from django.db import models

class Autores(models.Model):
	nombre = models.fields.CharField(
		max_length=45,
		null=False
	)
	apellidos = models.fields.CharField(
		max_length=45,
		null=False
	)

	def __unicode__(self):
		return "{} {}".format(self.nombre, self.apellidos)

