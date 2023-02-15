from django.shortcuts import render

# Create your views here.
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieListSerializer,MovieDetailSerializer,ReviewCreateSerializer ,CreateRatingSerializer
from  .service import get_client_ip


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request)))
        ).annotate(
            middle_star=models.Avg("ratings__star__value")
        )
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    def get(self, request, pk):
        try:

            movie = Movie.objects.get(id=pk)
            serializer = MovieDetailSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=404)


class ReviewCreateView(APIView):

    def post(self, request):
        review  =   ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
            return Response(status=201)
        else:
            return Response(status=400)


class AddStarRatingView(APIView):

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():

            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)
