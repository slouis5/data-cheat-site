from django.urls import path

from . import views

app_name = "cheat_sql"
urlpatterns = [
    path("", views.index, name="index"),
]