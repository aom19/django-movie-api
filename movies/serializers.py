

from rest_framework import serializers
from .models import Movie, Genre, Actor, Rating, Review


class MovieListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = ("id", "title", "tagline", "category", )


class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True),
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)


    class Meta:
        model = Movie
        exclude = ("draft", )



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
         