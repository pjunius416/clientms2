from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from clients.models import Client

class VehicleInformation(models.Model):
    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='vehicles',
    )
    make = models.CharField(max_length=50,blank=True, null=True, default=' ')
    model = models.CharField(max_length=50,blank=True, null=True, default=' ')
    vin_number = models.CharField(max_length=17,blank=True, null=True, default='')
    date_purchased = models.CharField(max_length=17,blank=True, null=True, default='')
    date_last_serviced = models.CharField(max_length=17,blank=True, null=True, default='')
    service_received = models.TextField(blank=True, null=True)
    serviced_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.vin_number or ''

    def get_absolute_url(self):
        return reverse('vehicle_detail', args=[str(self.id)])