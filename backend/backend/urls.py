"""backend URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog.views import manage_file, manage, home
from django.views.generic import TemplateView
from django.conf.urls import handler404, handler500


handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.page_error'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('api.urls')),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^sig/$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^test/$', manage_file, name='test'),
    url(r'^manage/$', manage),
    url(r'^$', home)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
