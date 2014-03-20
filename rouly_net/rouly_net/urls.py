from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import michel

handle404 = "error_404"
handle500 = "error_500"

urlpatterns = patterns('',

    url(r'^', include('michel.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
