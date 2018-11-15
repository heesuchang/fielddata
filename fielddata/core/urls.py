from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as core_views


urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
]