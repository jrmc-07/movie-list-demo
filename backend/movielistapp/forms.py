from django import forms
from movielistapp.models import Movie


class MovieForm(forms.ModelForm):
    """
    Form class for input validation
    """
    class Meta:
        model = Movie
        fields = ('title',)