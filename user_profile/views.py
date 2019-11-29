from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse
from .form import ExtendedUserCreationForm, ProfileForm
from user_profile.models import Profile
from auction.models import Auction

#  pip install django[bcrypt]

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        custom_form = ProfileForm(request.POST)
        if form.is_valid() and custom_form.is_valid():
            user = form.save()
            profile = custom_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account')
            return redirect('login')
        else:
            messages.error(request, ('Error occured:'))
    else: 
        form = ExtendedUserCreationForm()
        custom_form = ProfileForm()
            
    return render(request, 'user_profile/signup_form.html', {'form' : form, 'custom_form' : custom_form})

def user_view(request, username):
    user_account = get_object_or_404(get_user_model(), username = username)
    profile = Profile.objects.get(user = user_account)
    print(profile.dob)
    user_listings = Auction.objects.filter(seller=profile)
    print(user_listings)
    context = {
        'obj' : {
            'profile' : profile,
            'user_listings' : user_listings
        }
    }
    return render(request, 'user_profile/view_profile.html', context)

def login_view(request):
    context = {}
    return render(request, 'user_profile/login_form.html', context)

@login_required
def profile_view(request):
    profile = Profile.objects.get(user = request.user)
    won_bids = Auction.objects.filter(winner=profile)
    user_listings = Auction.objects.filter(seller=profile)

    context = {
        'obj' : {
            'won_bids' : won_bids,
            'user_listings' : user_listings
        }
    }
    return render(request, 'user_profile/my_profile.html', context)
