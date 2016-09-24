from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import EditorialForm
from .models import Editoriales


class CreateEditorialView(CreateView):
	form_class= EditorialForm
	success_url= '/editoriales/'
	template_name= 'editoriales/create.html'

class EditorialesListView(ListView):

	template_name = 'editoriales/listdelete.html'
	context_object_name = 'item_list'
	model = Editoriales

def delete_editoriales_view(request):
	# get post and perform action
	return_url = '/editoriales'
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
			editoriales = Editoriales.objects.filter(pk__in=list_of_input_ids)

			editoriales.delete()

			# return success url
			return HttpResponseRedirect(return_url)
	return HttpResponseBadRequest('Bad Request')