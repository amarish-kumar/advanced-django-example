from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^minus/(\d+)$', views.minus, name="minus"),
    url(r'^plus/(\d+)$', views.plus, name="plus"),
    url(r'^categoria/(\d+)$', views.categoria, name="categoria"),
    url(r'^add/$', views.add, name="add"),
]
