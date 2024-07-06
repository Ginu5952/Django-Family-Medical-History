from django.db import models
from django.utils import timezone
from apps.healthInsurance.models import HealthInsuranceCard
from django.db.models import Q, F
from apps.doctorDetails.models import DoctorDetail,Department
from apps.hospitalDetails.models import HospitalDetail
from django.core.exceptions import ValidationError


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
    date_of_visit = models.DateTimeField()
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

  #  def clean(self) :
          

     #   doctor_hospital_pairs = DoctorDetail.objects.values_list('doctor_id', 'doctor_name').distinct()

      #  for doctor_idd,doctor_namee in doctor_hospital_pairs:

           

        #    if doctor_idd == self.doctor_id.doctor_id:

          #      if self.doctor_id.hospital_id.hospital_id != self.hospital_id.hospital_id:

           #         raise ValidationError(f'{doctor_namee} is not associated with hospital id {self.hospital_id.hospital_id}. Please select a valid combination.')
           #     elif self.doctor_id.department !=  self.department.department:
          #          raise ValidationError(f'{doctor_namee} is not associated with {self.department.department}. Please select a valid combination.')

      
        
                    


   
    def __str__(self):
        return f'{self.health_insurance_card_no}   {self.diagnosis}   {self.doctor_id}   {self.date_of_visit}'    
