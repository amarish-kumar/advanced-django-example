from django.conf.urls import url, include
from django.views.generic import TemplateView

from views import EnlaceListView, EnlaceDetailView
from . import views
from app.views import EnlaceViewSet, UserViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'links', EnlaceViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.home, name="home"),
    url(r'^minus/(\d+)$', views.minus, name="minus"),
    url(r'^plus/(\d+)$', views.plus, name="plus"),
    url(r'^categoria/(\d+)$', views.categoria, name="categoria"),
    url(r'^add/$', views.add, name="add"),
    url(r'^about/$', TemplateView.as_view(template_name='index.html'),name="about"),
    url(r'^enlaces/$', EnlaceListView.as_view(),name="enlaces"),
    url(r'^enlace/(?P<pk>[\d]+)$', EnlaceDetailView.as_view(),name="enlace"),
]
