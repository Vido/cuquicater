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

# ViewSets define the view behavior.
class OfferViewSet(viewsets.ModelViewSet):
    queryset = NTOffer.objects.all()
    serializer_class = OfferSerializer
