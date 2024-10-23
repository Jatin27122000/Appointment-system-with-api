from django.urls import path
from appoint.views import AppointmentListCreateView, AppointmentDetailView

urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]
