"""elkbranch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from main.views import (
    index,
    codehub,
    project_detail,
    resume,
    contact,
    portfolio,
    portfolio_detail,
    about,
)

urlpatterns = [
    path('', index, name='home'),
    path('codehub/', codehub, name='codehub'),
    path("codehub/<int:pk>/", project_detail, name="project_detail"),
    path('resume/', resume, name='resume'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path("portfolio/<int:id>/", portfolio_detail, name="portfolio_detail"),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls)
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'media/(?P<path>.*)', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]
