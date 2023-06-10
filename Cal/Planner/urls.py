from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    url(r'^assign$', views.assign, name="assign"),
    path("upload", views.upload, name="upload"),
    path("download", views.download, name="download")
]