from django.contrib import admin
from appoint.models import Appointment



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ['name','phone_no','age','dob']