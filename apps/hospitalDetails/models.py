import re
from django.db import models
from django.core.exceptions import ValidationError

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

    def clean(self):
        super().clean()
        self.validate_contact_no()

    def validate_contact_no(self):
        pattern = r'^\d{9}$'
        if not re.match(pattern, self.contact_number):
            raise ValidationError("Contact number must be exactly 9 digits.")

    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.hospital_name}"
