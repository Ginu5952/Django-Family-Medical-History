from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from apps.healthInsurance.models import HealthInsuranceCard
from apps.familyMember.models import FamilyMember



class FamilyMedicalDetail(models.Model):
    
    visit_id = models.AutoField(primary_key=True)

    health_insurance_card_no = models.ForeignKey(
        HealthInsuranceCard,
        on_delete=models.CASCADE,
        db_column='health_insurance_card_no',
    )
    
    first_name = models.OneToOneField(FamilyMember,on_delete=models.CASCADE)

    doctor_id = models.ForeignKey(
        'doctorDetails.DoctorDetail',
        on_delete=models.CASCADE,
        db_column="doctor_id",
        related_name="doctor_visits"
    )

    date_of_visit = models.DateField()
    symptoms = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    medication = models.TextField(blank=True, null=True)

    class Meta:
        
        verbose_name_plural = 'Family Medical History'
        db_table = 'family_medical'
        constraints = [
           
            models.UniqueConstraint(
                fields=['health_insurance_card_no','first_name','doctor_id','date_of_visit'], 
                name='unique_doctor_visit'),

            models.CheckConstraint(
                check=models.Q(date_of_visit__lte=timezone.now().date()),
                name='Date of visit cannot be future date'
            ), 
        ]

    def clean(self):
            super().clean()

            # Ensure first name is associated with the selected health_insurance_card_no
            if self.first_name.health_insurance_card_no != self.health_insurance_card_no:
              
                raise ValidationError(f'{self.first_name} is not associated with {self.health_insurance_card_no}. Please select a valid combination.')

    
    
    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)        
                        

   
    def __str__(self):
        return f'{self.health_insurance_card_no}   {self.diagnosis}   {self.doctor_id}   {self.date_of_visit}'    
