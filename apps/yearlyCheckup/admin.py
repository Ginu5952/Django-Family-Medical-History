from django.contrib import admin
from .models import YearlyCheckUp


class YearlyCheckUpAdmin(admin.ModelAdmin):
  

    list_display = ('health_insurance_card_no', 'yearly_check_up_done', 'date_of_check_up')
  
admin.site.register(YearlyCheckUp,YearlyCheckUpAdmin)    


