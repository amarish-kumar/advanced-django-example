from django.conf.urls import url
from django.views.generic import TemplateView

from views import EnlaceListView, EnlaceDetailView
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^minus/(\d+)$', views.minus, name="minus"),
    url(r'^plus/(\d+)$', views.plus, name="plus"),
    url(r'^categoria/(\d+)$', views.categoria, name="categoria"),
    url(r'^add/$', views.add, name="add"),
    url(r'^about/$', TemplateView.as_view(template_name='index.html'),name="about"),
    url(r'^enlaces/$', EnlaceListView.as_view(),name="enlaces"),
    url(r'^enlace/(?P<pk>[\d]+)$', EnlaceDetailView.as_view(),name="enlace"),
]
