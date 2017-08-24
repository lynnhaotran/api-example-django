from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^auth/$', views.auth),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]