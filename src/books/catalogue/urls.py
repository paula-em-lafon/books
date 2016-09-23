from django.conf.urls import include, url

from .import views

urlpatterns = [
	url(r'^$', views.LibrosListView.as_view()),
	url(r'^libros/nuevo/$', views.CreateLibroView.as_view()),
	url(r'^libros/delete/$', views.delete_libros_view),
	url(r'^autores/$', views.AutoresListView.as_view()),
	url(r'^autores/nuevo/$', views.CreateAutorView.as_view()),
	url(r'^autores/delete/$', views.delete_autores_view),
	url(r'^editoriales/$', views.EditorialesListView.as_view()),
	url(r'^editoriales/nuevo/$', views.CreateEditorialView.as_view()),
	url(r'^editoriales/delete/$', views.delete_editoriales_view),

]
