import re
from django.db import models
from django.core.exceptions import ValidationError
from apps.healthInsurance.models import HealthInsuranceCard

class FamilyMember(models.Model):
    
    MARITAL_STATUS_CHOICES = {
    "Single": "Single",
    "Married": "Married",
    "Divorced": "Divorced",
    "Widowed" : "Widowed",
    "Separated" : "Separated",
    "Committed" : "Committed",
    "Other" : "Other"
    }

    member_id = models.AutoField(primary_key=True)
    health_insurance_card_no = models.ForeignKey(HealthInsuranceCard, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField()
    relation = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    marital_status = models.CharField(max_length=25, choices=MARITAL_STATUS_CHOICES)
    profession = models.CharField(max_length=20, null=True, blank=True)
    contact_no = models.CharField(max_length=15, unique=True)

    class Meta:
        constraints = [
        models.CheckConstraint(
        name='check_marital_status_valid',
        check=models.Q(marital_status__in=["Single", "Married", "Divorced", "Widowed", "Separated", "Committed", "Other"])
        )
        ]
        unique_together = (('health_insurance_card_no', 'first_name', 'relation'),)

    def clean(self):
        super().clean()
        self.validate_contact_no()

    def validate_contact_no(self):
        pattern = r'^\d{9}$'
        if not re.match(pattern, self.contact_no):
            raise ValidationError("Contact number must be exactly 9 digits.")

    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name