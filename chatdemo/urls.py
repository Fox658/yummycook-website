from django.conf.urls import url, include
#from django.contrib.auth import views as auth_views

from . import views

app_name = 'chatdemo'
#url(r'^register/$', views.RegisterView.as_view(), name='register'),url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
urlpatterns = [
    url(r'^chats/$', views.IndexView.as_view(), name='home_page'),   
]