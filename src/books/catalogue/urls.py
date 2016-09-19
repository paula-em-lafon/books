from django.conf.urls import include, url

from .views import CreateAutorView, CreateEditorialView, CreateLibroView
urlpatterns = [
    url(r'^autores/nuevo/', CreateAutorView.as_view()),
    url(r'^editoriales/nuevo/', CreateEditorialView.as_view()),
    url(r'^libros/nuevo/', CreateLibroView.as_view())
]
