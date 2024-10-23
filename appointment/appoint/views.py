from django.shortcuts import render
from rest_framework import generics
from appoint.models import Appointment
from appoint.serializers import AppointmentSerializer

# ListCreateAPIView: Handles GET (list all appointments) and POST (create a new appointment)
class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# RetrieveUpdateDestroyAPIView: Handles GET (retrieve), PUT/PATCH (update), DELETE (destroy)
class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

