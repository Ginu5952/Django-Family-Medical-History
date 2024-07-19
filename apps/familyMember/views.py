from django.shortcuts import render,redirect
from apps.familyMember.models import FamilyMember
from .forms import PostFamilyMemberForm
from . import models 
from django.contrib import messages


def family_member_home(request):

    members = FamilyMember.objects.all()
    # Pass the cards to the template context
    context = {
        'members': members
    }

    return render(request, 'family_members_home.html', context)

def member_post(request):
    if request.method == 'POST':
        form = PostFamilyMemberForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Save to database
            FamilyMember.objects.create(
                health_insurance_card_no=data['health_insurance_card_no'],
                first_name=data['first_name'],
                last_name=data.get('last_name', ''),  # Use get() to provide default value
                age=data['age'],
                relation=data['relation'],
                gender=data['gender'],
                marital_status=data['marital_status'],
                profession=data.get('profession', ''),  # Use get() to provide default value
                contact_no=data['contact_no']
            )
            messages.success(request, 'Family member added successfully!')
            return redirect('family-members:family_member_home')  # Redirect to the home page or other appropriate page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostFamilyMemberForm()

    context = {"form": form}
    return render(request, 'post_family_members.html', context)