from django.conf.urls import patterns, include, url
from django.conf import settings
from cmpds import views
# import django-batchimport

from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chemDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^create$', login_required(views.cmpdCreateView.as_view()), name='cmpd-create'),
    url(r'^(?P<pk>\d+)$',views.cmpdDetail, name='cmpd-detail'),
    url(r'^(?P<pk>\d+)/update$',login_required(views.cmpdUpdateView.as_view()), name='cmpd-update'),
    url(r'^(?P<pk>\d+)/delete$',login_required(views.cmpdDeleteView.as_view()), name='cmpd-delete'),
    # url(r'^batchimport/', include('batchimport.urls', namespace="batchimport")),
    url(r'^cmpdcsv/', views.cmpdCSV, name='CSV'),
)

# urlpatterns += patterns('', (
#         r'^static/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': settings.STATIC_ROOT}
# ))

# urlpatterns += patterns('',
#                (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#                  {'document_root': settings.MEDIA_ROOT}),
#               )