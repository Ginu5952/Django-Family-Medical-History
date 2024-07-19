from django.urls import path
from . import views

app_name = 'family-members'

urlpatterns = [
    path('', views.family_member_home, name='family_member_home'),
    path('add/',views.member_post, name='post_family_member')
]
