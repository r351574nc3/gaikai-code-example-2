from django.conf.urls import patterns, include, url

from itrservices import views

urlpatterns = patterns('',

    url(r'^routers/$', views.all_routers, name = 'all routers'),
    url(r'^routers/(?P<router>.+)/$', views.routers_by_name, name = 'routers by name'),
    url(r'^continents/$', views.continents, name = 'continents')
)
