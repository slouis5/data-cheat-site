from django.urls import path

from . import views

app_name = "cheat_py"

urlpatterns = [
    path("", views.index, name="index"),
]