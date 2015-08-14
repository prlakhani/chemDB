from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from chemDB import views     # This lets us use the custom error handlers, as well as an index view with context, if desired.

# These handlers override the default error page provided by Django.
# Django looks for these var names specifically in the urlconf.

handler404 = 'chemDB.views.page_not_found'
handler500 = 'chemDB.views.server_error'

from django.views.generic import TemplateView, RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chemDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^search/', include('haystack.urls')),
    url(r'^cmpds/', include('cmpds.urls', namespace="cmpds")),
    # url(r'^batchimport/', include('batchimport.urls')),
    url(r'^excel/', include('excel.urls')),
)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
))

urlpatterns += patterns('',
               (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
              )