from django.db import models
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

    def __str__(self):
        return self.first_name
