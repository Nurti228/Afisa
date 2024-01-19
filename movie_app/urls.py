from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_api_view),
    path('<int:id>/', views.movie_detail_api_view),
    path('director/', views.director_list_api_view),
    path('director/<int:id>/', views.director_detail_api_view),
    path('review/', views.review_list_api_view),
    path('review/<int:id>/', views.review_detail_api_view),
]

