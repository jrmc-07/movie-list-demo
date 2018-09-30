import json

from django.core.serializers import serialize
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View

from movielistapp.forms import MovieForm
from movielistapp.models import Movie


@method_decorator(csrf_exempt, name='dispatch')
class MovieList(View):
    """
    List all movies, or create a new movie entry.
    """
    def get(self, request):
        """
        Returns all movies.
        """
        movies = Movie.objects.all()
        return HttpResponse(serialize("json", movies),
                            content_type="application/json")

    @csrf_exempt
    def post(self, request):
        """
        Creates a new movie entry.
        """
        form = MovieForm(json.loads(request.body.decode('utf-8')))
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)