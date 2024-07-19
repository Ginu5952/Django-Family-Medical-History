from django.urls import path
from . import views

app_name = 'health-insurance'

urlpatterns = [
    path('', views.health_insurance_home, name='health_insurance_home'),
     path('', views.index, name='index'),
]
