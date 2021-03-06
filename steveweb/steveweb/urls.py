from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='main_home'),
    url(r'^user/', include('user.urls')),
    url(r'^649/', include('sixfournine.urls')),
    url(r'^nhl/', include('nhl.urls')),
)

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name = 'steveweb_login'),

    url(r'^logout/$', 'logout',
        {'next_page': '/'},
        name = 'steveweb_logout'),
)
