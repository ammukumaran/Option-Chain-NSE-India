from django.db import models
# Create your models here.


class CE(models.Model):
    timestamp = models.CharField(max_length=100)
    strikePrice = models.CharField(max_length=100)
    openInterest = models.CharField(max_length=100)
    changeinOpenInterest = models.CharField(max_length=100)
    totalTradedVolume = models.CharField(max_length=100)
    impliedVolatility = models.CharField(max_length=100)
    lastPrice = models.CharField(max_length=100)
    change = models.CharField(max_length=100)
    pChange = models.CharField(max_length=100)
    bidQty = models.CharField(max_length=100)
    bidprice = models.CharField(max_length=100)
    askQty = models.CharField(max_length=100)
    askPrice = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'CE'

    def __str__(self):
        return self.timestamp


class PE(models.Model):
    timestamp = models.CharField(max_length=100)
    strikePrice = models.CharField(max_length=100)
    openInterest = models.CharField(max_length=100)
    changeinOpenInterest = models.CharField(max_length=100)
    totalTradedVolume = models.CharField(max_length=100)
    impliedVolatility = models.CharField(max_length=100)
    lastPrice = models.CharField(max_length=100)
    change = models.CharField(max_length=100)
    pChange = models.CharField(max_length=100)
    bidQty = models.CharField(max_length=100)
    bidprice = models.CharField(max_length=100)
    askQty = models.CharField(max_length=100)
    askPrice = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'PE'

    def __str__(self):
        return self.timestamp
