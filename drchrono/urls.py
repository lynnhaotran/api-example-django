from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^auth/$', views.auth),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^show_patients/$', views.show_patients, name='show_patients'),
    url(r'^checkin/$', views.checkin, name='checkin'),
    url(r'^get_patient/$', views.get_patient, name='get_patient'),
    url(r'^demographics/$', views.demographics, name='demographics'),
    url(r'^update_demographics/$', views.update_demographics),
    url(r'^allset/$', views.allset, name='allset'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]