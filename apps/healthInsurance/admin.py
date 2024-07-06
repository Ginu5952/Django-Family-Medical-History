
from django.contrib import admin
from .models import HealthInsuranceCard


class HealthInsuranceAdmin(admin.ModelAdmin):
  

    list_display = ('health_insurance_card_no', 'expiry_date_of_card')
  
admin.site.register(HealthInsuranceCard,HealthInsuranceAdmin)    
