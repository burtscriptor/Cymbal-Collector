from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cymbals/", views.index, name="index"),
    path("cymbal/<int:cymbal_id>", views.details, name="details"),
    path("cymbal/create", views.CreateCymbal.as_view(), name='create_cymbal'),
    path("cymbal/<int:pk>/delete/", views.CymbalDelete.as_view(), name="cymbal_delete"),
    path("cymbal/<int:pk>/update/", views.CymbalUpdate.as_view(), name='cymbal_update'),
]