from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import michel

handler404 = "michel.views.error"
handler500 = "michel.views.error"

urlpatterns = patterns('',

    url(r'^', include('michel.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
