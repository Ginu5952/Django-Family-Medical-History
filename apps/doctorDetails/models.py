from django.db import models
from apps.hospitalDetails.models import HospitalDetail
from django.contrib.postgres.fields import ArrayField


class DoctorDetail(models.Model):
    
    
    doctor_id = models.AutoField(primary_key=True)
    hospital_id = models.IntegerField()
    department = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, null=True,blank=True,choices=[('M', 'Male'), ('F', 'Female')])
    availability_days = ArrayField(models.CharField(max_length=20),null=True, blank=True)
    
    consultation_hours = models.JSONField(default=list, null=True, blank=True) 
    contact_no = models.CharField(max_length=15, unique=True,null=True,blank=True)


    hospital_id = models.ForeignKey(
        HospitalDetail,
        on_delete=models.CASCADE,
        db_column='hospital_id',  
    )

    class Meta:
        unique_together = ('doctor_id', 'hospital_id', 'department')
       

    def __str__(self):
        return f"Doctor id:{self.doctor_id}  Name:{self.doctor_name}  Department:{self.department}  {self.hospital_id}"
