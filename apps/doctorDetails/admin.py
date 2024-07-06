from django.contrib import admin
from .models import DoctorDetail, Department, DoctorDepartment




@admin.register(DoctorDetail)
class DoctorDetailAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'availability_days', 'contact_no')
    search_fields = ('doctor_name', 'contact_no')
    
