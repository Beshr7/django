from django.urls import path

from . import views

app_name = "targets"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
