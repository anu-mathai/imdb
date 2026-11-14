"""
URL configuration for imbd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from film.views import MovieListCreateView
from film.views import MovieRetrieveUpdateDeleteView
from accounts.views import AdmincreateView
from accounts.views import UserRegisterView
from music.views import SongCreateView
from evaluation.views import ReviewCreateView
from evaluation.views import ReviewRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',MovieListCreateView.as_view()),
    path('movies/<int:pk>/',MovieRetrieveUpdateDeleteView.as_view()),

    path("owner/register/",AdmincreateView.as_view()),
    path('user/register/',UserRegisterView.as_view()),

    path('m/<int:pk>/song/',SongCreateView.as_view()),

    path('movie/<int:pk>/review/',ReviewCreateView.as_view()),
    path('review/<int:pk>/',ReviewRetrieveUpdateDeleteView.as_view()),
]
