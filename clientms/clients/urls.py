from django.urls import path
from . import views
from .views import (ClientListView, ClientUpdateView, ClientDetailView, ClientDeleteView, ClientCreateView, CommentUpdateView)

urlpatterns = [
    path('<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('<int:pk>/comments/add', CommentUpdateView.as_view(), name='comment_new'),
    path('', ClientListView.as_view(), name='client_list'),
]