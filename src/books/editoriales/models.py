from django.db import models


class Editoriales(models.Model):
	nombre = models.fields.CharField(
		max_length = 45
	)
	sede = models.fields.CharField(
		max_length = 45
	)
	
	def __unicode__(self):
		return self.nombre