from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^post_url/$', views.post_resume, name = 'post_resume'),
    url(r'^login/$', views.login_view, name='Login'),
    url(r'^logout/$', views.logout_view, name='Logout'),
    url(r'^show/$', views.show, name = 'show'),
    url(r'^superuser/$', views.superu, name = 'superuser'),
    url(r'^newuser/$', views.newuser, name='newuser'),
    url(r'^gandp/$', views.gandp, name='gandp'),
    url(r'^reqhr/(?P<usr>\w+)/$', views.reqhr, name='reqhr'),
    url(r'^reqacc/(?P<usr>\w+)/$', views.reqacc, name='reqacc'),
]
