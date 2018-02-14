from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^series/(?P<slug>[-\w]+)/$',views.detalle_tutorial_series, name="detalle_tutorial_series"),
    url(r'^series/$', views.serie_tutoriales_list, name = "serie_tutoriales_list_view"),
    url(regex=r'^series/(?P<slug>[-\w]+)/$', view=views.detalle_tutorial_series, name="detalle_tutorial_series"),
    url(regex=r'^series/(?P<serie_tutoriales>[-\w]+)/(?P<slug>[-\w]+)/$', view=views.detalle_leccion, 
    name="detalle_leccion"),

]