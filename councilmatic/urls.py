"""councilmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from haystack.query import SearchQuerySet
from councilmatic_core.views import CouncilmaticSearchForm, CouncilmaticFacetedSearchView
from miamidade.views import *

sqs = SearchQuerySet().facet('bill_type')\
                      .facet('sponsorships', sort='index')\
                      .facet('controlling_body')\
                      .facet('inferred_status')\
                      .facet('topics')\
                      .facet('legislative_session')\
                      .highlight()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', CouncilmaticFacetedSearchView(searchqueryset=sqs,
                                       form_class=CouncilmaticSearchForm)),
    url(r'^$', MiamiDadeIndexView.as_view(), name='index'),
    url(r'^about/$', MiamiDadeAboutView.as_view(), name='about'),
    url(r'^legislation/(?P<slug>.*)/$', MiamiDadeBillDetailView.as_view(), name='bill_detail'),
    url(r'^commissioners/$', MiamiDadeCouncilMembersView.as_view(), name='council_members'),
    url(r'', include('councilmatic_core.urls')),
    url(r'^council-members/$', RedirectView.as_view(url='/commissioners/', permanent=True), name='council_members'),
]

