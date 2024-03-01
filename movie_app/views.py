from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers, models


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movie = models.Movie.objects.all()
        data = serializers.MovieSerializer(movie, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = serializers.MovieUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        print(request.data)

        # print(request.data)
        # title = request.data.get('title')
        # description = request.data.get('description')
        # duration = request.data.get('duration')
        # director_id = request.data.get('directors')

        # models.Movie.objects.create(title=title,
        #                             description=description,
        #                             duration=duration,
        #                             director_id=director_id)

        movie = models.Movie.objects.create(**request.data)
        return Response(data=serializers.MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie_id = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(data={'error': 'Movie does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.MovieSerializer(movie_id).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Movie has been deleted'})
    elif request.method == 'PUT':
        movie_id.title = request.data.get('title')
        movie_id.description = request.data.get('description')
        movie_id.duration = request.data.get('duration')
        movie_id.director_id = request.data.get('director_id')
        movie_id.save()
        return Response(data=serializers.MovieSerializer(movie_id).data)


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        director = models.Director.objects.all()
        data = serializers.DirectorSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':

        serializer = serializers.DirectorUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

        director = models.Director.objects.create(**request.data)
        return Response(data=serializers.DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(data={'error': 'Director does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Director has been deleted'})
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=serializers.DirectorSerializer(director).data)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = models.Review.objects.all()
        data = serializers.ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':

        serializer = serializers.ReviewUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

        review = models.Review.objects.create(**request.data)
        return Response(data=serializers.ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        reviews = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(data={'error': 'Review does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.ReviewSerializer(reviews).data
        return Response(data=data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Review has been deleted'})
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.movie_id = request.data.get('movie_id')
        reviews.stars = request.data.get('stars')
        reviews.save()
        return Response(data=serializers.ReviewSerializer(reviews).data)
