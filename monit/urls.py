from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^collector$', views.collector, name='monit_collector'),
    url(r'^servers/$', views.server_list, name='server_list'),
    url(r'^servers/(?P<server_name>\w+)/$', views.server_detail, name='server_detail'),
    url(r'^servers/(?P<server_name>\w+)/processes/(?P<process_name>[\w\-\.]+)/$', views.process_detail, name='process_detail'),

]
