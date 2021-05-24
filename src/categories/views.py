import json
from pathlib import Path

import pandas as pd
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoriesAPIView(APIView):
    """
        STATIC JSON
    """
    def get(self, request):
        categories_path = (Path(__file__).parent / 'categories_dataset.csv').resolve()
        csv_file = pd.read_csv(categories_path)
        data = csv_file.to_json(orient="records")
        return Response(json.loads(data))

class BrandAPIView(APIView):
    """
        STATIC JSON FOR BRANDS
    """
    def get(self, request):
        brands_path = (Path(__file__).parent / 'brands-neotrust.csv').resolve()
        csv_file = pd.read_csv(brands_path)
        data = csv_file.to_json(orient="records")
        return Response(json.loads(data))

class UniqueProductAPIView(APIView):
    """
        DATABASE / SEARCH ENGINE DATA
    """
    def get(self, request):
        return Response({'some': 'data'})

