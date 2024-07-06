from django.contrib import admin
from .models import FamilyMember



class FamilyMemberAdmin(admin.ModelAdmin):
  

    list_display = ('health_insurance_card_no', 'first_name', 'last_name','age','relation', 'gender','marital_status','profession','contact_no')
  
admin.site.register(FamilyMember,FamilyMemberAdmin)    