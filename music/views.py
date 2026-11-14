from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from music.serializers import SongSerializer
from film.models import Movie

# Create your views here.
class SongCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk=None):

        movie_object=get_object_or_404(Movie,id=pk)

        form_data=request.data

        serializer_instance=SongSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(movie=movie_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

