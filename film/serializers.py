from rest_framework import serializers
from film.models import Movie
from music.models import Song
from music.serializers import SongSerializer
from evaluation.models import Review
from evaluation.serializers import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):

    song_count=serializers.SerializerMethodField(read_only=True)

    songs=serializers.SerializerMethodField(read_only=True)

    review_count=serializers.SerializerMethodField(read_only=True)

    reviews=serializers.SerializerMethodField(read_only=True)

    class Meta:

        model=Movie

        fields="__all__"

        read_only_fields=["id"]


    def get_song_count(self,obj):

            return Song.objects.filter(movie=obj).count()

    def get_songs(self,obj):

         song_objects=Song.objects.filter(movie=obj)

         serializer_instance=SongSerializer(song_objects,many=True)

         return serializer_instance.data

    def get_review_count(self,obj):

         return Review.objects.filter(movie=obj).count()

    def get_reviews(self,obj):

         review_objects=Review.objects.filter(movie=obj)

         serializer_instance=ReviewSerializer(review_objects,many=True)

         return serializer_instance.data

