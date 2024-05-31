from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.views import *

from user import views

urlpatterns = [

    path('register/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
