from django.contrib import admin
from .models import DoctorDetail, Department



admin.site.register(Department)


@admin.register(DoctorDetail)
class DoctorDetailAdmin(admin.ModelAdmin):
    list_display = ('doctor_id','doctor_name', 'availability_days','consultation_hours', 'contact_no')
    search_fields = ('doctor_name', 'contact_no')
    
