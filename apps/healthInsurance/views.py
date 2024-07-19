from django.shortcuts import render
from .models import HealthInsuranceCard

# Create your views here.

def index(request):
    return render(request, 'index.html')

def health_insurance_home(request):

    cards = HealthInsuranceCard.objects.all()
    # Pass the cards to the template context
    context = {
        'cards': cards
    }

    return render(request, 'health_insurance_home.html', context)

def index(request):
    return render(request, 'index.html')