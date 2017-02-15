"""core_perfomance_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from project.apps.users import views as user_views


urlpatterns = [
    url(r'^users/$', user_views.UserListView.as_view(), name="user_list"),
    url(r'^user/(?P<pk>\d+)/$', user_views.UserDetailView.as_view(), name="user_detail"),
    url(r'^user/(?P<pk>\d+)/update/$', user_views.UserUpdateView.as_view(), name="user_update"),
    url(r'^user/create/$', user_views.UserCreateView.as_view(), name="user_create"),
    url(r'^user/(?P<pk>\d+)/delete/$', user_views.UserDeleteView.as_view(), name="user_delete"),
    url(r'^users/export/$', user_views.UserExportView.as_view(), name="user_export"),
    url(r'^admin/', admin.site.urls),
]
