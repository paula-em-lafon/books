from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import AutorForm
from .models import Autores


# Create your views here.
class CreateAutorView(CreateView):
	'''
	create new author vieww
	'''

	form_class= AutorForm
	success_url= '/autores/'
	template_name= 'autores/create.html'
	title = "Crear Autor"


class AutoresListView(ListView):
	'''
	Listar autores
	'''
	template_name = 'autores/listdelete.html'
	context_object_name = 'item_list'
	model = Autores


def delete_autores_view(request):
	'''
	 borrar autores
	'''
	# get post and perform action
	return_url = '/autores'
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
			autores = Autores.objects.filter(pk__in=list_of_input_ids)

			autores.delete()

			# return success url
			return HttpResponseRedirect(return_url)
	return HttpResponseBadRequest('Bad Request')