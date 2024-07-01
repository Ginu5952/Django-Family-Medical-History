from django.db import models
from django.utils import timezone
from django.db import models
from apps.healthInsurance.models import HealthInsuranceCard




class ChildrenCheckUp(models.Model):

    check_up_id = models.AutoField(primary_key=True)
    health_insurance_card_no = models.ForeignKey(HealthInsuranceCard, on_delete=models.CASCADE)
    parents_name = models.CharField(max_length=50)
    number_of_children = models.IntegerField(null=True, blank=True, default=0)
    children_name_and_age = models.JSONField(null=True,blank=True)
    vaccination_completed = models.JSONField(null=True,blank=True)
    date_of_vaccination = models.JSONField(null=True,blank=True)
    vaccination_name = models.JSONField(null=True,blank=True)


    class Meta:
        unique_together = ('health_insurance_card_no','parents_name')

     

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        today = timezone.now().date()
         
        if self.number_of_children != 0:
            for child, completed in self.vaccination_completed.items():
                if not completed:  # If vaccination is not completed
                    if self.date_of_vaccination.get(child):  # Check if there's a date entered
                        raise ValidationError(f"Date of vaccination for {child} cannot be specified if vaccination is not completed.")
                    if self.vaccination_name.get(child):  # Check if there's a vaccination name entered
                        raise ValidationError(f"Vaccination name for {child} cannot be specified if vaccination is not completed.")
                else:  # If vaccination is completed
                    date_str = self.date_of_vaccination.get(child)
                    if date_str:
                        date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
                        if date > today:
                            raise ValidationError(f"Date for {child} cannot be in the future.")
                    

    def __str__(self):
        # Assume vaccination_details is a dictionary like {"child1": True, "child2": False}
        vaccination_status = self.vaccination_completed
        parent_str = f"{self.parents_name}'s children vaccination status: "
        children_status = []
        if vaccination_status:
            for child, status in vaccination_status.items():
                status_str = "completed" if status else "not completed"
                children_status.append(f"{child} vaccination {status_str}")
        
        return parent_str + ", ".join(children_status)  



       