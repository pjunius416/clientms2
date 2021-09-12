from django.views.generic import ListView
from .models import VehicleInformation

class VehicleListView(ListView):
    model = VehicleInformation
    template_name = 'vehicle_list.html'
