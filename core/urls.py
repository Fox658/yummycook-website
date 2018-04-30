from django.conf.urls import url

from . import views

app_name='core'
urlpatterns = [
    url(r'^accounts/update/$', views.edit_user, name='account_update'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
]