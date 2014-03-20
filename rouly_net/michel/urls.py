from django.conf.urls import patterns, include, url

urlpatterns = patterns('michel.views',

    url(r'^$', 'home', name = 'home'),
    url(r'^work$', 'work', name = 'work'),
    url(r'^research$', 'research', name = 'research'),
    url(r'^volunteer$', 'volunteer', name = 'volunteer'),
    url(r'^contact$', 'contact', name = 'contact'),

)
