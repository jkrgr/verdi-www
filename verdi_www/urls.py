from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import news


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'verdi_www.views.home', name='home'),
    # url(r'^verdi_www/', include('verdi_www.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'verdi.views.main_view'),
    url(r'^nyheter', 'news.views.news_view'),
    url(r'^portefolje', 'market.views.portfolio_view'),

)
