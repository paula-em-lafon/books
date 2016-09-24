from django.conf.urls import include, url

from .import views

urlpatterns = [
	url(r'^autores/$', views.AutoresListView.as_view()),
	url(r'^autores/nuevo/$', views.CreateAutorView.as_view()),
	url(r'^autores/delete/$', views.delete_autores_view),
]
