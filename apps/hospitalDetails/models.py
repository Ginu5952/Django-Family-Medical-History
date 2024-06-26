from django.db import models

class HospitalDetail(models.Model):
    
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15, unique=True,null=True,blank=True)
    website = models.CharField(max_length=25,unique=True,null=True,blank=True)
    registration_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('hospital_name','location','address')



    def __str__(self) -> str:
        return f"Hospital_id:{self.hospital_id} | Hospital_name:{self.hospital_name}"
