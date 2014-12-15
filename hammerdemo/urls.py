from django.conf.urls import patterns, include, url
from hammerdemo.views import (
    
    DemopersonsiblingsListView,
    DemopersonsiblingsDetailView,
    DemopersonsiblingsCreateView,
    DemopersonsiblingsUpdateView,
    DemopersonsiblingsDeleteView,
    
    DemopersonListView,
    DemopersonDetailView,
    DemopersonCreateView,
    DemopersonUpdateView,
    DemopersonDeleteView,
    
    DemopersonparentsListView,
    DemopersonparentsDetailView,
    DemopersonparentsCreateView,
    DemopersonparentsUpdateView,
    DemopersonparentsDeleteView,
    
    DemofamilypetsListView,
    DemofamilypetsDetailView,
    DemofamilypetsCreateView,
    DemofamilypetsUpdateView,
    DemofamilypetsDeleteView,
    
    DemofamilyListView,
    DemofamilyDetailView,
    DemofamilyCreateView,
    DemofamilyUpdateView,
    DemofamilyDeleteView,
    
    DemofamilymembersListView,
    DemofamilymembersDetailView,
    DemofamilymembersCreateView,
    DemofamilymembersUpdateView,
    DemofamilymembersDeleteView,
    
    DemopetListView,
    DemopetDetailView,
    DemopetCreateView,
    DemopetUpdateView,
    DemopetDeleteView,
    
    DemopersonchildrenListView,
    DemopersonchildrenDetailView,
    DemopersonchildrenCreateView,
    DemopersonchildrenUpdateView,
    DemopersonchildrenDeleteView,
    
)

urlpatterns = patterns(
    '',

    url(r'^demopersonsiblings/$', DemopersonsiblingsListView.as_view(), name="demopersonsiblings_list"),
    url(r'^demopersonsiblings/(?P<pk>\d+)$', DemopersonsiblingsDetailView.as_view(), name="demopersonsiblings_detail"),
    url(r'^demopersonsiblings/create/$', DemopersonsiblingsCreateView.as_view(), name="demopersonsiblings_create"),
    url(r'^demopersonsiblings/update/(?P<pk>\d+)$', DemopersonsiblingsUpdateView.as_view(), name="demopersonsiblings_update"),
    url(r'^demopersonsiblings/delete/(?P<pk>\d+)$', DemopersonsiblingsDeleteView.as_view(), name="demopersonsiblings_delete"),

    url(r'^demoperson/$', DemopersonListView.as_view(), name="demoperson_list"),
    url(r'^demoperson/(?P<pk>\d+)$', DemopersonDetailView.as_view(), name="demoperson_detail"),
    url(r'^demoperson/create/$', DemopersonCreateView.as_view(), name="demoperson_create"),
    url(r'^demoperson/update/(?P<pk>\d+)$', DemopersonUpdateView.as_view(), name="demoperson_update"),
    url(r'^demoperson/delete/(?P<pk>\d+)$', DemopersonDeleteView.as_view(), name="demoperson_delete"),

    url(r'^demopersonparents/$', DemopersonparentsListView.as_view(), name="demopersonparents_list"),
    url(r'^demopersonparents/(?P<pk>\d+)$', DemopersonparentsDetailView.as_view(), name="demopersonparents_detail"),
    url(r'^demopersonparents/create/$', DemopersonparentsCreateView.as_view(), name="demopersonparents_create"),
    url(r'^demopersonparents/update/(?P<pk>\d+)$', DemopersonparentsUpdateView.as_view(), name="demopersonparents_update"),
    url(r'^demopersonparents/delete/(?P<pk>\d+)$', DemopersonparentsDeleteView.as_view(), name="demopersonparents_delete"),

    url(r'^demofamilypets/$', DemofamilypetsListView.as_view(), name="demofamilypets_list"),
    url(r'^demofamilypets/(?P<pk>\d+)$', DemofamilypetsDetailView.as_view(), name="demofamilypets_detail"),
    url(r'^demofamilypets/create/$', DemofamilypetsCreateView.as_view(), name="demofamilypets_create"),
    url(r'^demofamilypets/update/(?P<pk>\d+)$', DemofamilypetsUpdateView.as_view(), name="demofamilypets_update"),
    url(r'^demofamilypets/delete/(?P<pk>\d+)$', DemofamilypetsDeleteView.as_view(), name="demofamilypets_delete"),

    url(r'^demofamily/$', DemofamilyListView.as_view(), name="demofamily_list"),
    url(r'^demofamily/(?P<pk>\d+)$', DemofamilyDetailView.as_view(), name="demofamily_detail"),
    url(r'^demofamily/create/$', DemofamilyCreateView.as_view(), name="demofamily_create"),
    url(r'^demofamily/update/(?P<pk>\d+)$', DemofamilyUpdateView.as_view(), name="demofamily_update"),
    url(r'^demofamily/delete/(?P<pk>\d+)$', DemofamilyDeleteView.as_view(), name="demofamily_delete"),

    url(r'^demofamilymembers/$', DemofamilymembersListView.as_view(), name="demofamilymembers_list"),
    url(r'^demofamilymembers/(?P<pk>\d+)$', DemofamilymembersDetailView.as_view(), name="demofamilymembers_detail"),
    url(r'^demofamilymembers/create/$', DemofamilymembersCreateView.as_view(), name="demofamilymembers_create"),
    url(r'^demofamilymembers/update/(?P<pk>\d+)$', DemofamilymembersUpdateView.as_view(), name="demofamilymembers_update"),
    url(r'^demofamilymembers/delete/(?P<pk>\d+)$', DemofamilymembersDeleteView.as_view(), name="demofamilymembers_delete"),

    url(r'^demopet/$', DemopetListView.as_view(), name="demopet_list"),
    url(r'^demopet/(?P<pk>\d+)$', DemopetDetailView.as_view(), name="demopet_detail"),
    url(r'^demopet/create/$', DemopetCreateView.as_view(), name="demopet_create"),
    url(r'^demopet/update/(?P<pk>\d+)$', DemopetUpdateView.as_view(), name="demopet_update"),
    url(r'^demopet/delete/(?P<pk>\d+)$', DemopetDeleteView.as_view(), name="demopet_delete"),

    url(r'^demopersonchildren/$', DemopersonchildrenListView.as_view(), name="demopersonchildren_list"),
    url(r'^demopersonchildren/(?P<pk>\d+)$', DemopersonchildrenDetailView.as_view(), name="demopersonchildren_detail"),
    url(r'^demopersonchildren/create/$', DemopersonchildrenCreateView.as_view(), name="demopersonchildren_create"),
    url(r'^demopersonchildren/update/(?P<pk>\d+)$', DemopersonchildrenUpdateView.as_view(), name="demopersonchildren_update"),
    url(r'^demopersonchildren/delete/(?P<pk>\d+)$', DemopersonchildrenDeleteView.as_view(), name="demopersonchildren_delete"),

)

