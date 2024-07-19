
from django.core.validators import RegexValidator
from django.db import models


class HospitalDetail(models.Model):
    
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15, unique=True,null=True,blank=True, validators=[RegexValidator(regex=r'^\d{9}$', message="Contact number must be exactly 9 digits.")])
    website = models.CharField(max_length=25,unique=True,null=True,blank=True)
   

    class Meta:
        unique_together = ('hospital_name','location','address')
        verbose_name_plural = 'Hospital Details'
        db_table = 'hospital_details'

    
    def __str__(self) -> str:
        return f"{self.hospital_name}"
