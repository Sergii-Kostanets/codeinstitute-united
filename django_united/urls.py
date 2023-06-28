"""django_united URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import account_settings
from django.conf.urls import handler404, handler403, handler500
from django.conf import settings
from .views import page_not_found_local, server_error

handler404 = 'django_united.urls.page_not_found_local'
handler403 = 'django_united.urls.page_not_found_local'
handler500 = 'django_united.urls.server_error'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('connect.urls'), name='connect_urls'),
    path('blog/', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),
    path('googleee4e9b2810051589.html', TemplateView.as_view(template_name='googleee4e9b2810051589.html')),
    path('account/settings/', account_settings, name='account_settings'),
]

if settings.DEBUG:
    urlpatterns += [
        path('404', page_not_found_local, name='404'),
        path('500', server_error, name='500'),
    ]
