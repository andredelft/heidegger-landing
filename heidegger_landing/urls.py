from .views import home_view

from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("", home_view, name="home"),
]

if settings.DEBUG:
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
