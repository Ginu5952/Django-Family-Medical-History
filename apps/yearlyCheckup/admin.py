from django.contrib import admin
from .models import YearlyCheckUp


class YearlyCheckUpAdmin(admin.ModelAdmin):
  

    list_display = ('get_name_first_name', 'get_name_last_name', 'yearly_check_up_done', 'date_of_check_up')
    search_fields = ('name__first_name', 'name__last_name')
    ordering = ('name__first_name', 'name__last_name')

    def get_name_first_name(self, obj):
        return obj.name.first_name
    get_name_first_name.admin_order_field = 'name__first_name'
    get_name_first_name.short_description = 'First Name'

    def get_name_last_name(self, obj):
        return obj.name.last_name
    get_name_last_name.admin_order_field = 'name__last_name'
    get_name_last_name.short_description = 'Last Name'
  
admin.site.register(YearlyCheckUp,YearlyCheckUpAdmin)    


