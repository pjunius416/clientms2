from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import VehicleInformation
from django.urls import reverse_lazy

class VehicleListView(LoginRequiredMixin, ListView):
    model = VehicleInformation
    template_name = 'vehicle_list.html'

class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = VehicleInformation
    template_name = 'vehicle_detail.html'
    login_url = 'login'
    
class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleInformation
    fields = ('make', 'model', 'date_last_serviced', 'service_received', 'serviced_by')
    template_name = 'vehicle_edit.html'
    
class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = VehicleInformation
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')
    
class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = VehicleInformation
    template_name = 'vehicle_new.html'
    fields = ('client', 'make', 'model', 'date_last_serviced', 'service_received', 'serviced_by')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)