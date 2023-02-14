from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieListSerializer,MovieDetailSerializer,ReviewCreateSerializer


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(draft=False)

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
        review  =    ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
            return Response(status=201)
        else:
            return Response(status=400)
