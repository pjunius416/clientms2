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
    make = models.CharField(max_length=50,blank=False, null=False, default=' ')
    model = models.CharField(max_length=50,blank=False, null=False, default=' ')
    vin_number = models.CharField(max_length=17,blank=True, null=True, default='')
    date_purchased = models.DateTimeField(auto_now_add=True)
    date_last_serviced = models.DateTimeField(auto_now_add=True)
    service_received = models.CharField(max_length=300)
    serviced_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.vin_number

    def get_absolute_url(self):
        return reverse('Client_list')