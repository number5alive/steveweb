from django.conf.urls import patterns, include, url


urlpatterns = patterns('nhl.views',
    url(r'^$', 'home', name='nhl_home'),
    url(r'^home$', 'home', name='nhl_home'),
)
