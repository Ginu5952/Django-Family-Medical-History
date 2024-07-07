from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from apps.doctorDetails.models import DoctorDetail,Department
from apps.hospitalDetails.models import HospitalDetail
from apps.healthInsurance.models import HealthInsuranceCard



class FamilyMedicalDetail(models.Model):
    
    visit_id = models.AutoField(primary_key=True)

    health_insurance_card_no = models.ForeignKey(
        HealthInsuranceCard,
        on_delete=models.CASCADE,
        db_column='health_insurance_card_no',
    )
    
    
    doctor_id = models.ForeignKey(
        DoctorDetail,
        on_delete=models.CASCADE,
        db_column="doctor_id",
        related_name="doctor_visits"
    )

    hospital_id = models.ForeignKey(
        HospitalDetail,
        on_delete=models.CASCADE,
        db_column="hospital_id",
        related_name="hospital_visits"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        db_column="department",
        
    )
    date_of_visit = models.DateField()
    symptoms = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    medication = models.TextField(blank=True, null=True)

    class Meta:
        
     
        constraints = [
           
            models.UniqueConstraint(
                fields=['health_insurance_card_no','doctor_id', 'hospital_id', 'department','date_of_visit'], 
                name='unique_doctor_visit'),

            models.CheckConstraint(
                check=models.Q(date_of_visit__lte=timezone.now().date()),
                name='Date of visit cannot be future date'
            ), 
        ]

    def clean(self):
            super().clean()

            # Ensure doctor is associated with the selected hospital
            if self.doctor_id.hospital.hospital_name != self.hospital_id.hospital_name:
              
                raise ValidationError(f'{self.doctor_id.doctor_name} is not associated with {self.hospital_id}. Please select a valid combination.')


            # Ensure doctor is associated with the selected department
            if  self.doctor_id.departments != self.department:
                raise ValidationError(f'{self.doctor_id.doctor_name} is not associated with department {self.department}. Please select a valid combination.')

    
    
    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)        
                        

   
    def __str__(self):
        return f'{self.health_insurance_card_no}   {self.diagnosis}   {self.doctor_id}   {self.date_of_visit}'    
