from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

from django.http import HttpResponse


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^registration/login/$', views.login, name='login'),
    #url(r'^registration/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    url(r'^googlea55e63331b4c4a8a\.html$', lambda r: HttpResponse("google-site-verification: googlea55e63331b4c4a8a.html", content_type="text/plain")),
]