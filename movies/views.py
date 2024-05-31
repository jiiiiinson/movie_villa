from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Category, Review
from .forms import MovieForm, AddForm, ReviewForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def index(request):
    query = request.GET.get('query', '')
    error_message = ''
    movies = []

    if query:
        print(f"Query: {query}")
        movies = Movie.objects.filter(
            Q(name__icontains=query) | Q(category__cname__icontains=query)
        )
        print(f"Movies: {movies}")

        if not movies.exists():
            error_message = "No movies found"
    else:
        movies = Movie.objects.all()
        print(f"All Movies: {movies}")

    return render(request, 'index.html', {
        'query': query,
        'movies': movies,
        'error_message': error_message,
    })


# def index(request):
#     search_query = request.GET.get('query', '')
#     error_message = ''
#     if search_query:
#         movies = Movie.objects.filter(
#             Q(name__icontains=search_query) |
#             Q(category__cname__icontains=search_query)
#         )
#     if not search_query.exists():
#         error_message = "No movies found"
#     else:
#         movies = Movie.objects.all()
#
#     context = {
#         'movies': movies
#     }
#     return render(request, 'index.html', context)


@login_required(login_url='/')
def add_film(request):
    if request.method == 'POST':
        form = AddForm(request.POST or None, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('/')
    else:
        form = AddForm()
    return render(request, 'add.html', {'form': form})


def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if movie.user != request.user:
        return redirect('/')  # or return an error response
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    movie = get_object_or_404(Movie, id=id)

    # Check if the logged-in user is the owner of the movie
    if movie.user != request.user:
        return redirect('/')  # or return an appropriate error response

    if request.method == 'POST':
        movie.delete()
        return redirect('/')

    return render(request, 'delete.html', {'movie': movie})


@login_required(login_url='/')  # Redirect to home page if not logged in
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    try:
        # Try to get the existing review
        review = Review.objects.get(movie=movie, user=request.user)
    except Review.DoesNotExist:
        review = None
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('detail', movie_id=movie.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review.html', {'form': form})


def review_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'detail.html', {'movie': movie, 'reviews': reviews})
