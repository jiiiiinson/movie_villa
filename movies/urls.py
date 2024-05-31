from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('movie/<int:movie_id>/', views.review_detail, name='detail'),
    path('add/', views.add_film, name='add_film'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('review/<int:movie_id>/', views.add_review, name='review'),
    path('search/', views.index, name='search'),
]
