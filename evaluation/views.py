from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from film.models import Movie
from evaluation.models import Review
from evaluation.serializers import ReviewSerializer

# Create your views here.
class ReviewCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,pk=None):

        movie_objects=get_object_or_404(Movie,id=pk)

        form_data=request.data

        serializer_instance=ReviewSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(movie=movie_objects,owner=request.user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

class ReviewRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        instance=get_object_or_404(Review,id=pk,owner=request.user)

        serializer_instance=ReviewSerializer(instance)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        instance=get_object_or_404(Review,id=pk,owner=request.user)

        form_data=request.data

        serializer_instance=ReviewSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        instance=get_object_or_404(Review,id=pk,owner=request.user)  

        instance.delete()  

        response_data={"message":"deleted"}

        return Response(response_data)


        



        