from django.contrib import admin
from apps.medicalExpenseDetails.models import MedicalExpensesDetail,Medicines,MedicalBill


class MedicalBillInline(admin.StackedInline):
    model = MedicalBill
    extra = 0
    readonly_fields = ['bill_image']

    

class MedicineAdmin(admin.ModelAdmin):

    list_display = ('medicine_name', 'price_per_quantity', 'get_currency_type')

    def get_currency_type(self, obj):
        return obj.currency
    get_currency_type.short_description = 'Currency'



class MedicalExpenseAdmin(admin.ModelAdmin):

    
    list_display = ('get_date_of_visit', 'get_first_name','get_last_name','get_diagnosis', 'medicine_list', 'quantity', 'get_total_price')

    def get_date_of_visit(self, obj):
        return obj.family_medical_detail.date_of_visit
    get_date_of_visit.short_description = 'Date of Visit'


    def get_first_name(self, obj):
        return obj.family_medical_detail.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.family_medical_detail.last_name
    get_last_name.short_description = 'Last Name'


    def get_diagnosis(self, obj):
        return obj.family_medical_detail.diagnosis
    get_diagnosis.short_description = 'diagnosis'


    def medicine_list(self, obj):
        return ", ".join(medicine.medicine_name for medicine in obj.medicine_prescribed .all())
    medicine_list.short_description = 'Prescribed Medicines'  

    def get_total_price(self, obj):
        total_price = sum(medicine.price_per_quantity * obj.quantity for medicine in obj.medicine_prescribed.all())
        currency = obj.medicine_prescribed.first().currency if obj.medicine_prescribed.exists() else 'N/A'
        return f'{total_price} {currency}'
    get_total_price.short_description = 'Total Price' 

    
admin.site.register(MedicalBill)    
admin.site.register(Medicines,MedicineAdmin)
admin.site.register(MedicalExpensesDetail,MedicalExpenseAdmin)   

 