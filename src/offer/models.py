from django.db import models

# Create your models here.

class NTOffer(models.Model):
    """
        JSON Offer
        - Comes from ClearSale transaction
    """
    OrderID = models.CharField(max_length=2048, unique=True)
    OrderSellerID = models.IntegerField()
    OriginID = models.IntegerField()
    Sku = models.IntegerField()
    #Ean = models.IntegerField(blank=True, null=True)
    Description = models.CharField(max_length=2048)
    Quantity = models.DecimalField(max_digits=15, decimal_places=2)
    Value = models.DecimalField(max_digits=15, decimal_places=2)
    CategoryIDSeller = models.IntegerField(blank=True, null=True)
    # CategorySeller ?
    # RawProductArray ?
    legal_name = models.CharField(max_length=2048)
    # displayName  = models.CharField(max_length=2048)
    siteLink = models.URLField(max_length=4096)
    ecommerce_url = models.URLField(max_length=4096)
