from django.conf.urls import url
from . import views 



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^usecontrol/add/$', views.usecontrol_add, name='usecontrol_add'),
    url(r'^usecontrol/list/$', views.UseControlView.as_view()),
    url(r'vehicle$', views.VehicleList.as_view(), name='vehicle_list'),
    url(r'vehicle/add$', views.VehicleCreate.as_view(), name='vehicle_create'),
    url(r'vehicle/(?P<pk>\d+)$', views.VehicleUpdate.as_view(), name='vehicle_update'),
    url(r'vehicle/(?P<pk>\d+)/delete/$', views.VehicleDelete.as_view(), name='vehicle_delete'),
]
