from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),

    url(r'^api/(?P<pk>[0-9]+)/highlight/$', views.ApiHighlight.as_view()),

    url(r'^api/$',
        views.ApiList.as_view(),
        name='api-list'),
    url(r'^api/(?P<pk>[0-9]+)/$',
        views.ApiDetail.as_view(),
        name='api-detail'),
    url(r'^api/(?P<pk>[0-9]+)/highlight/$',
        views.ApiHighlight.as_view(),
        name='api-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^profile/$',
        views.ProfileList.as_view(),
        name='profile-list'),
    url(r'^profile/(?P<pk>[0-9]+)/$',
        views.ProfileDetail.as_view(),
        name='profile-detail'),

    url(r'^connectlog/$',
        views.ConnectLogList.as_view(),
        name='connectlog-list'),
    url(r'^connectlog/(?P<pk>[0-9]+)/$',
        views.ConnectLogDetail.as_view(),
        name='connectlog-detail'),

    url('^profile/(?P<badge>.+)/$', views.ProfileList.as_view()),
    url('^profile/(?P<user>.+)/$', views.ProfileList.as_view()),

])
