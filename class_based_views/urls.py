from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListAPIView.as_view()),
    path('movies/<int:id>/', views.MovieUpdateDeleteApiView.as_view()),
    path('reviews/', views.ReviewListAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewUpdateDeleteApiView.as_view()),
    path('directors/', views.DirectorListAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorUpdateDeleteApiView.as_view()),
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
]
