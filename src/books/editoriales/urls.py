from django.conf.urls import include, url

from .import views

urlpatterns = [
	url(r'^editoriales/$', views.EditorialesListView.as_view()),
	url(r'^editoriales/nuevo/$', views.CreateEditorialView.as_view()),
	url(r'^editoriales/delete/$', views.delete_editoriales_view),

]
