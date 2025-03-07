from django.urls import path

from . import views

app_name = "cheat_sql"
urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>/", views.chapter_ui, name="chapter_ui"),
    path("<slug:slug>/<slug:slug2>/", views.lesson_ui, name="lesson_ui"),
]