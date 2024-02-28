from rest_framework import serializers
from .models import Movie, Director, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie author stars rating'.split()
