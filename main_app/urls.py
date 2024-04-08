from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cymbals/", views.index, name="index"),
    path("cymbal/<int:cymbal_id>", views.details, name="details")
]