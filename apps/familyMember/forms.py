from django import forms 
from apps.healthInsurance.models import HealthInsuranceCard
from apps.familyMember.models import FamilyMember
from django.core.validators import RegexValidator

class PostFamilyMemberForm(forms.Form):

    health_insurance_card_no = forms.ModelChoiceField(
    queryset=HealthInsuranceCard.objects.all(),
    widget=forms.Select(
        attrs={
            "class": "card-input",
            "placeholder": "Select Health Insurance Card"
        }
    ),
    label="Health Insurance Card"
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "first-input",
                "placeholder": "Enter First Name"
            }
        ),
        label="First Name"
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "last-input",
                "placeholder": "Enter Last Name"
            }
        ),
        label="Last Name"
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "age-input",
                "placeholder": "Enter Age"
            }
        ),
        label="Age"
    )

    relation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "relation-input",
                "placeholder": "Enter Relation"
            }
        ),
        label="Relation"
    )

    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female')],
        widget=forms.Select(
            attrs={
                "class": "gender-input"
            }
        ),
        label="Gender"
    )

    marital_status = forms.ChoiceField(
        choices=FamilyMember.MARITAL_STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "marital-status-input"
            }
        ),
        label="Marital Status"
    )

    profession = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profession-input",
                "placeholder": "Enter Profession"
            }
        ),
        label="Profession"
    )

    contact_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "contact-input",
                "placeholder": "Enter Contact Number"
            }
        ),
        label="Contact Number",
        validators=[RegexValidator(regex=r'^\d{9}$', message="Contact number must be exactly 9 digits.")]
    )
