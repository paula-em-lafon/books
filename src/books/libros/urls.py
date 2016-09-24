from django.conf.urls import include, url

from .import views

urlpatterns = [
	url(r'^$', views.LibrosListView.as_view()),
	url(r'^libros/nuevo/$', views.CreateLibroView.as_view()),
	url(r'^libros/delete/$', views.delete_libros_view),
]
