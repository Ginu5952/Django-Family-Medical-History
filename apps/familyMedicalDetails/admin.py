from django.contrib import admin

from .models import FamilyMedicalDetail


class MedicalCheckUpAdmin(admin.ModelAdmin):
  

    list_display = ('health_insurance_card_no', 'get_full_name', 'doctor', 'diagnosis', 'date_of_visit')

    def get_full_name(self, obj):
        return obj.full_name
    get_full_name.short_description = 'Full Name'
  
admin.site.register(FamilyMedicalDetail,MedicalCheckUpAdmin)    