from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import michel

handle404 = "michel.views.error"
handle500 = "michel.views.error"

urlpatterns = patterns('',

    url(r'^', include('michel.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
