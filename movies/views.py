from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
from .models import Movie, Actor
from .serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,
    ActorListSerializer,
    ActorDetailSerializer
)
from .service import get_client_ip,MovieFilter


class MovieListView(generics.ListAPIView):
    serializer_class = MovieListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Avg("ratings__star__value")
        )
        return movies


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer


class AddStarRatingView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))




class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
