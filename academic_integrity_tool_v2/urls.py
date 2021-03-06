"""academic_integrity_tool_v2 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from lti_provider import views as lti_views
from policy_wizard import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lti/launch', views.determine_role_view, name='determine_role'),
    path('lti/config.xml', lti_views.LTIConfigView.as_view(), name="get_lti_xml"),
    path('', include('policy_wizard.urls')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

