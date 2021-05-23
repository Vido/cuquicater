from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    """
    """

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.DO_NOTHING,
            blank=True,
            null=True,
            related_name='create')

    updateed_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.DO_NOTHING,
            blank=True,
            null=True,
            related_name='update')


class NTQueue(BaseModel):
    """
        Classification Batches
    """
    Description = models.CharField(max_length=2048)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
    )


class NTOffer(models.Model):
    """
        JSON Offer
        - Comes from ClearSale transaction
    """
    queue = models.ForeignKey(NTQueue, null=True, blank=True, on_delete=models.SET_NULL)
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


class HumanClassification(BaseModel):
    """
        JSON Offer
        - Comes from ClearSale transaction
    """
    ntoffer = models.ForeignKey(NTOffer,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                default=None)
    category = models.CharField(max_length=2048)
    brand = models.CharField(max_length=2048)
    unique_product = models.CharField(max_length=2048)
