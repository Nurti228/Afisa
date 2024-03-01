from rest_framework import serializers
from .models import Movie, Director, Review
from rest_framework.exceptions import ValidationError


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


class MovieUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField()
    duration = serializers.FloatField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f'Director with id {director_id} does not exist')


class DirectorUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=20)


class ReviewUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count() == 0:
            raise ValidationError(f'Movie with id {movie_id} does not exist')
