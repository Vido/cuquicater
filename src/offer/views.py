from random import randint

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets

from offer.models import NTOffer

# Serializers define the API representation.
class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NTOffer
        fields = [
            'OrderID',
            'OrderSellerID',
            'OriginID',
            'Sku',
            'Description',
            'Quantity',
            'Value',
            'CategoryIDSeller',
            'legal_name',
            'siteLink',
            'ecommerce_url',
        ]

class OfferViewSet(viewsets.ModelViewSet):
    queryset = NTOffer.objects.all()
    serializer_class = OfferSerializer


class OfferAPIView(APIView):
    """
    """
    def get(self, request):
        """
            Calls selection strategy
        """
        qs = NTOffer.objects.all()
        ridx = randint(0, qs.count() -1)
        obj = qs[ridx]
        serializer = OfferSerializer(obj)
        return Response(serializer.data)

    def post(self, request):
        """
            Recieves user data
            - TODO
        """
        return Response({'data': 'ok'})
