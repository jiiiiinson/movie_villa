from django import forms
from .models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'poster', 'actors', 'category', 'trailer_link']


class AddForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'poster', 'actors', 'category', 'trailer_link']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'review', 'rating']
