from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cymbals/', views.index, name='index'),
  
    path('cymbals/<int:cymbal_id>/', views.details, name='details'),
    path('cymbal/create', views.CreateCymbals.as_view(), name='create_cymbals'),
    path('cymbal/<int:cymbal_id>/add_hire/', views.add_hire, name='add_hire'),
    path('cymbal/<int:pk>/delete/', views.CymbalDelete.as_view(), name='cymbal_delete'),
    path('cymbal/<int:pk>/update/', views.CymbalUpdate.as_view(), name='cymbal_update'),
    path('cymbal/<int:cymbal_id>/add_artist/<int:artist_id>/', views.add_artist, name='add_artist'),
    path('cymbal/<int:cymbal_id>/remove_artist/<int:artist_id>/', views.remove_artist, name='remove_artist'),

    path('artist/', views.IndexArtist.as_view(), name='index_artist'),
    path('artist/<int:pk>/detail/', views.Artists_Detail.as_view(), name='artists_detail'),
    path('artist/create', views.CreateArtist.as_view(), name='create_artist'),
    path('artist/<int:pk>/update/', views.UpdateArtist.as_view(), name='update_artist'),
    path('artist/<int:pk>/delete/', views.DeleteArtist.as_view(), name='delete_artist'),
   
]