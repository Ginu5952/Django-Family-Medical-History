from django.contrib import admin
from .models import ChildrenDetail, VaccinationName, ChildrenCheckUp

admin.site.register(ChildrenDetail)
admin.site.register(VaccinationName)


class ChildrenCheckUpAdmin(admin.ModelAdmin):
  

    list_display = ('father_name','mother_name', 'number_of_children', 'children_names_list', 'vaccination_completed', 'vaccination_names_list','date_of_vaccination')
    list_filter = ('vaccination_completed', 'date_of_vaccination')
    search_fields = ('father_name__first_name', 'mother_name__first_name', 'children_name__first_name', 'children_name__last_name')
    
    def children_names_list(self, obj):
        return ", ".join(child.first_name for child in obj.children_name.all())
    children_names_list.short_description = 'Children Names'    


    def vaccination_names_list(self, obj):
        return ", ".join(child.vaccination_name for child in obj.vaccination_name.all())
    vaccination_names_list.short_description = 'Vaccination Names'   

admin.site.register(ChildrenCheckUp,ChildrenCheckUpAdmin)    