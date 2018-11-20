from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
	url(r'^logout/$', auth_views.LogoutView.as_view, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
]