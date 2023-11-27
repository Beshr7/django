from django.urls import path

from . import views

app_name = "flowless"

urlpatterns = [
    path("", views.flowlessPage, name="flowlesspage"),
]
