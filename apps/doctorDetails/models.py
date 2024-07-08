from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.hospitalDetails.models import HospitalDetail



class Department(models.Model):
    department = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.department




class DoctorDetail(models.Model):

    DAY_CHOICES = [
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    ]


    doctor_id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(HospitalDetail, on_delete=models.CASCADE)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    doctor_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=[('M', 'Male'), ('F', 'Female')])
    availability_days = MultiSelectField(choices=DAY_CHOICES, null=True, blank=True, max_choices=7, max_length=14, help_text="Select multiple days using Ctrl or Cmd key")
    consultation_hours = models.JSONField(default=list, null=True, blank=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True,validators=[RegexValidator(regex=r'^\d{9}$', message="Contact number must be exactly 9 digits.")])

    class Meta:
        ordering = ['doctor_id'] 
  
    def __str__(self):
        return self.doctor_name


