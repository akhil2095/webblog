from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
	login, logout, password_reset, password_reset_done, password_reset_confirm,
	passwird_reset_complete)

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'blog/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'blog/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^change_password/$', views.change_password, name='change_password'),
	url(r'^reset-password/$', password_reset, name='reset_password'),
	url(r'^reset-password/done$', password_reset_done, name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset-password/complete$', password_reset_complete, name='password_reset_complete')	
]

# for reset-password/confirm run the host server in cmd: python -m smtpd -n -c DebuggingServer localhost:1025