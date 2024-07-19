from django.db import models


class Medicines(models.Model):

    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR', 'Indian Rupee'),
        ('GBP', 'British Pound'),
      
    ]
    
    medicine_name = models.CharField(max_length=50)
    price_per_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR')


    def __str__(self):
        return f'{self.medicine_name} {self.price_per_quantity}'

    class Meta:
        verbose_name_plural = 'Medicines'

class MedicalExpensesDetail(models.Model):

      
    family_medical_detail = models.OneToOneField(
        'familyMedicalDetails.FamilyMedicalDetail',
        related_name='medical_expenses_detail',
        on_delete=models.CASCADE
    )

    medicine_prescribed = models.ManyToManyField(
        'medicalExpenseDetails.Medicines',
        related_name='medical_expenses_details'
    )
    
    quantity = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return f'{self.family_medical_detail.first_name}'


    class Meta:
        verbose_name_plural = 'Medical Expenses Details'


class MedicalBill(models.Model):
    medical_expenses_detail = models.OneToOneField(
        'medicalExpenseDetails.MedicalExpensesDetail',
        related_name='medical_bill',
        on_delete=models.CASCADE
    )
    bill_image = models.ImageField(upload_to='medical_bills/', blank=True, null=True)


    def __str__(self):
        return f'{self.medical_expenses_detail.family_medical_detail.first_name} {self.medical_expenses_detail.family_medical_detail.last_name}'