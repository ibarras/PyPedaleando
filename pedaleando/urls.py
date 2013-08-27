from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pedaleando.views.home', name='home'),
    # url(r'^pedaleando/', include('pedaleando.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^$', include('evento.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^evento/$', include('evento.urls')),
)

#Setting para servir fotos 
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
            #(r'^media_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT#, 'show_indexes':True#}),
)

