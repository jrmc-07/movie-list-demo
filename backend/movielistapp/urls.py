from django.urls import path
from movielistapp import views

urlpatterns = [
    path('movies', views.MovieList.as_view()),
    path('movies/<int:movie_id>', views.MovieDetails.as_view()),
    path('movies/<int:movie_id>/like', views.movieLikes),
]
