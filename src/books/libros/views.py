from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .forms import LibroMultiForm
from .models import Libros, AutoresHasLibros

# Create your views here.
class CreateLibroView(FormView):
	success_url= '/'
	form_class= LibroMultiForm
	template_name= 'libros/create.html'

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

		return HttpResponseRedirect(self.get_success_url())


class LibrosListView(ListView):

	template_name = 'libros/listdelete.html'
	context_object_name = 'item_list'
	model = AutoresHasLibros


def delete_libros_view(request):
	# get post and perform action
	return_url = '/'
	if request.method == 'POST':
		action = request.POST.get('perform')

		#verify perform is delete
		if action == 'delete':
			list_of_input_ids=request.POST.getlist('checkboxed')

			# if no checkboxes marked return same page
			if not list_of_input_ids:
				return HttpResponseRedirect(return_url)

			# get input ids cast them to ints and get list of AutoresHasLibros objects
			list_of_input_ids = map(int, list_of_input_ids)
			autores_has_libros = AutoresHasLibros.objects.filter(pk__in=list_of_input_ids)

			# get books related to autores_has_libros
			isbns = autores_has_libros.values_list('libros_isbn_id', flat=True)
			libros =  Libros.objects.filter(isbn__in=isbns)

			#delete libros and autores
			autores_has_libros.delete()
			libros.delete()

			# return success url
			return HttpResponseRedirect(return_url)
	return HttpResponseBadRequest('bad request')