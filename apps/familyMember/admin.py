from django.contrib import admin
from .models import FamilyMember



class FamilyMemberAdmin(admin.ModelAdmin):
  
    search_fields = ('first_name', 'last_name')
    list_display = ('health_insurance_card_no', 'get_uppercase_first_name','age','relation', 'gender','marital_status','profession','contact_no')


    def get_uppercase_first_name(self, obj):
        return obj.first_name.upper()
    get_uppercase_first_name.short_description = 'First Name'



   # def get_uppercase_last_name(self, obj):
   #     return obj.last_name.upper()
  #  get_uppercase_last_name.short_description = 'Last Name'
  
admin.site.register(FamilyMember,FamilyMemberAdmin)    