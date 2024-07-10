
from django.core.validators import RegexValidator
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
    health_insurance_card_no = models.OneToOneField('healthInsurance.HealthInsuranceCard', related_name='healthInsurance', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField()
    relation = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    marital_status = models.CharField(max_length=25, choices=MARITAL_STATUS_CHOICES)
    profession = models.CharField(max_length=20, null=True, blank=True)
    contact_no = models.CharField(max_length=15, unique=True,validators=[RegexValidator(regex=r'^\d{9}$', message="Contact number must be exactly 9 digits.")])

    class Meta:
        constraints = [
        models.CheckConstraint(
        name='check_marital_status_valid',
        check=models.Q(marital_status__in=["Single", "Married", "Divorced", "Widowed", "Separated", "Committed", "Other"])
        )
        ]
        unique_together = (('health_insurance_card_no', 'first_name', 'relation'),)
        ordering = ['health_insurance_card_no']
        verbose_name_plural = 'Family Member Details'
        db_table = 'family_member'


    def __str__(self):
        return self.first_name