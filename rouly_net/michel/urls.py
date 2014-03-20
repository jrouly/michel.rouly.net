from django.conf.urls import patterns, include, url

urlpatterns = patterns('michel.views',

    url(r'^$', 'home', name = 'home'),
    url(r'^work$', 'work', name = 'work'),
    url(r'^research$', 'research', name = 'research'),
    url(r'^community$', 'community', name = 'community'),
    url(r'^contact$', 'contact', name = 'contact'),

    url(r'^resume.pdf$', 'resume', name = 'resume'),

)
