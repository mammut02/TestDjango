from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.get_post, name='post'),
    url(r'^publisher/$', views.get_publisher, name='publisher'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^login$', views.connection, name='login'),
    url(r'^logout$', views.log_out, name='logout')
)