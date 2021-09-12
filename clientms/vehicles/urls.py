from django.urls import path
from . import views
from .views import VehicleListView

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle_list'), 
]