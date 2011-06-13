from django.contrib import admin
from django.conf.urls.defaults import *
from main import views as main_views
from meeting import views as meeting_views
import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', meeting_views.new, name='new'),
    url(r'^meeting/(?P<meeting_id>.*)$', meeting_views.meeting, name='meeting'),
    url(r'^all/$', meeting_views.all, name='all'),
    (r'^admin/', include(admin.site.urls)),    
    url(r'^site-media/(?P<path>.*)$',       'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),    
    url(r'^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes':True}),        

)
