from rest_framework import serializers
from .models import Movie, Director, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class MovieSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title description duration directors'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie author stars rating'.split()
