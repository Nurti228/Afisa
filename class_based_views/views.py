from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from movie_app import models
from movie_app import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserCreateSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegisterAPIView(APIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(username=username, password=password)
        return Response(data={'message': 'User created successfully'},
                        status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key},
                            status=status.HTTP_200_OK)
        return Response(data={'error': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)


class MovieListAPIView(ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'


class ReviewListAPIView(ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filterset_fields = ['stars']


class ReviewUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'


class DirectorListAPIView(ListCreateAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer


class DirectorUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = 'id'
