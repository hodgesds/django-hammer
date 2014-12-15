from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView, DemoView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hammer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^demo$', DemoView.as_view(), name='demo'),
    url(r'^hammer/', include('hammerdemo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),

)

urlpatterns += (url(r'^$', include('angular.urls')),)