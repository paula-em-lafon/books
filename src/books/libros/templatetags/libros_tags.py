from django import template
from books.libros.models import Libros
register = template.Library()


@register.simple_tag
def get_libro(pk, attr):
	obj = getattr(Libros.objects.get(isbn=pk), attr)
	return obj