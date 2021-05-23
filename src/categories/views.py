from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoriesAPIView(APIView):
    """
        STATIC JSON
    """
    def get(self, request):
        return Response({'some': 'data'})

class BrandAPIView(APIView):
    """
        STATIC JSON
    """
    def get(self, request):
        return Response({'some': 'data'})

class UniqueProductAPIView(APIView):
    """
        DATABASE / SEARCH ENGINE DATA
    """
    def get(self, request):
        return Response({'some': 'data'})

