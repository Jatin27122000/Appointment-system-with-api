from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()  
    phone_no = models.CharField(max_length=15)
    
    def __str__(self):
        return f"Appointment for {self.name}"
