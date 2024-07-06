from django.db import models
from apps.hospitalDetails.models import HospitalDetail
from django.contrib.postgres.fields import ArrayField


class Department(models.Model):
    department = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.department



class DoctorDetail(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(HospitalDetail, on_delete=models.CASCADE)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    doctor_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=[('M', 'Male'), ('F', 'Female')])
    availability_days = ArrayField(models.CharField(max_length=20), null=True, blank=True)
    consultation_hours = models.JSONField(default=list, null=True, blank=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.doctor_name


