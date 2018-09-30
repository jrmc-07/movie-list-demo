from django.urls import path
from movielistapp import views

urlpatterns = [
    path('movies', views.MovieList.as_view()),
]