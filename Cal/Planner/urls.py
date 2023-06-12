from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("assign", views.assign, name="assign"),
    path("upload", views.upload, name="upload"),
    path("download", views.download, name="download"),
    path("edit/<str:id>", views.edit, name="edit")
]