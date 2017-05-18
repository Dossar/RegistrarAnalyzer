from django.conf.urls import url

from . import views

app_name = 'registrar_analyzer'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^professor', views.ProfessorView.as_view(), name='professor'),
]
