from django.contrib import admin

from .models import FamilyMedicalDetail


class MedicalCheckUpAdmin(admin.ModelAdmin):
  

    list_display = ('health_insurance_card_no','first_name', 'doctor_id','diagnosis', 'date_of_visit')
  
admin.site.register(FamilyMedicalDetail,MedicalCheckUpAdmin)    