from django.contrib import admin

from .models import FamilyMedicalDetail




class MedicalCheckUpAdmin(admin.ModelAdmin):
  

    list_display = ('health_insurance_card_no', 'doctor_id', 'department','diagnosis', 'date_of_visit','hospital_id')
  
admin.site.register(FamilyMedicalDetail,MedicalCheckUpAdmin)    