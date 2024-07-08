from django.db import models
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from apps.healthInsurance.models import HealthInsuranceCard
from apps.familyMember.models import FamilyMember


class ChildrenDetail(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class VaccinationName(models.Model):

    vaccination_name = models.CharField(max_length=20,null=True,blank=True)
 
    def __str__(self) -> str:
        return f'{self.vaccination_name}'
     

class ChildrenCheckUp(models.Model):

    check_up_id = models.AutoField(primary_key=True)
    health_insurance_card_no = models.OneToOneField(HealthInsuranceCard, on_delete=models.CASCADE)
    father_name = models.ForeignKey(FamilyMember,related_name='father_checkups', on_delete=models.CASCADE)
    mother_name = models.ForeignKey(FamilyMember, related_name='mother_checkups',on_delete=models.CASCADE)
    number_of_children = models.IntegerField( default=1)
    children_name =  models.ManyToManyField(ChildrenDetail, related_name='check_ups')
    vaccination_completed = models.BooleanField(default=False)
    date_of_vaccination = models.DateField(null=True,blank=True)
    vaccination_name = models.ManyToManyField(VaccinationName, related_name='children_vaccinations',blank=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['health_insurance_card_no', 'father_name', 'mother_name'],
                name='unique_checkup_per_family'
            ),
            models.CheckConstraint(
                check=models.Q(date_of_vaccination__lte=timezone.now().date()),
                name='vaccination date cannot be future date'
            ),    
        ]
     
    def clean(self):
    
        
        if self.health_insurance_card_no != self.father_name.health_insurance_card_no:
            raise ValidationError(f'{self.father_name} is not associated with {self.health_insurance_card_no}. Please select a valid combination.')

    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)  
        
            
    def __str__(self):
       
        children_names = ", ".join(child.first_name for child in self.children_name.all())
        return f'CheckUp {self.check_up_id} for {self.health_insurance_card_no.health_insurance_card_no} with children: {children_names}'

    def parents_name(self):
       
        return f'{self.father_name.name} & {self.mother_name.name}'