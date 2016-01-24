from django.conf.urls import url
import os

from . import views

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

app_name = 'MainApp'
urlpatterns = [
    url(r'^$', view = views.IndexView, name='index'),
]