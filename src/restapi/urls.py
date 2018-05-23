from django.conf.urls import url
from restapi import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    #url(r'^testgetquery/$',views.TestView.as_view()),
   # url(r'^testpostquery$',views.TestView.as_view()),
    #url(r'^testauth$',views.TestAuthView.as_view()),
    url(r'^onDemandStories$',views.CircleViewSet.as_view({'get': 'list'}))
]