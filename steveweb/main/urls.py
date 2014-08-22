from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^home$', 'home', name='main_home')
)
