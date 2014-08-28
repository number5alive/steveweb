from django.conf.urls import patterns, include, url


urlpatterns = patterns('sixfournine.views',
    url(r'^$', 'home', name='sixfournine_home'),
    url(r'^home$', 'home', name='sixfournine_home'),
)
