from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

class HealthInsuranceCard(models.Model):
    health_insurance_card_no = models.CharField(max_length=50, primary_key=True)
    expiry_date_of_card = models.DateField()

    def __str__(self):
        return self.health_insurance_card_no

    def clean(self):
        if self.expiry_date_of_card <= timezone.now().date():
            raise ValidationError('The expiry date must be in the future.')

    def save(self, *args, **kwargs):
        # Convert expiry_date_of_card string to datetime.date if it's a string
        if isinstance(self.expiry_date_of_card, str):
            self.expiry_date_of_card = datetime.datetime.strptime(self.expiry_date_of_card, '%Y-%m-%d').date()

        self.clean()  # Run validation
        super().save(*args, **kwargs)  # Call the original save method

