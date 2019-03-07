from django.urls import path
from . import views


# url paths

urlpatterns = [
    path("", views.index, name="index"),
    path("welcome/", views.welcome, name="welcome"),
    path("thankYou/", views.thankYou, name="thankYou")
]