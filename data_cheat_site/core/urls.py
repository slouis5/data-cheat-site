from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.ContributorsView.as_view(), name="about"),
]