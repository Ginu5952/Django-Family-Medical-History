import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.healthInsurance.models import HealthInsuranceCard

class YearlyCheckUp(models.Model):

    yearly_check_up_id = models.AutoField(primary_key=True)
    health_insurance_card_no = models.ForeignKey(HealthInsuranceCard, on_delete=models.CASCADE)
    yearly_check_up_done = models.BooleanField(default=False)
    date_of_check_up = models.DateField(null=True,blank=True)

    
    class Meta:
        constraints = [
            models.CheckConstraint(
                name='check_yearly_check_up_done_valid',
                check=models.Q(yearly_check_up_done__in=[True, False])
            ),
            models.CheckConstraint(
                name='check_date_of_check_up_valid',
                check=(
                    models.Q(date_of_check_up__isnull=True) |
                    models.Q(date_of_check_up__lte=timezone.now().date())
                )
            ),
            models.UniqueConstraint(
                fields=['health_insurance_card_no', 'date_of_check_up'],
                name='unique_health_insurance_card_date_of_check_up'
            )
        ]

    def clean(self):
        if self.yearly_check_up_done:
            if not self.date_of_check_up:
                raise ValidationError('Date of check-up must be set if yearly check-up is done.')
            if self.date_of_check_up > timezone.now().date():
                raise ValidationError('The date of check-up cannot be a future date.')
        else:
            if self.date_of_check_up is not None:
                raise ValidationError('Date of check-up must be null if yearly check-up is not done.')

    def save(self, *args, **kwargs):
       
        if isinstance(self.date_of_check_up, str):
            self.date_of_check_up = datetime.datetime.strptime(self.date_of_check_up, '%Y-%m-%d').date()
        self.clean()  # Run validation
        super().save(*args, **kwargs) 

    def __str__(self):
        
        if self.yearly_check_up_done:
            return f"Yearly Check-Up for {self.health_insurance_card_no} on {self.date_of_check_up}"
        else:
            return f"{self.health_insurance_card_no} not done yearly checkup" 