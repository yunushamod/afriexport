import json
from pprint import pprint
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.conf import settings
import requests
# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        country = request.POST.get('country')
        state = request.POST.get('state')
        user_form = UserRegistrationForm(data = request.POST, files=request.FILES)
        if user_form.is_valid() and (country or state):
            cd = user_form.cleaned_data
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user, phone=cd['phone'], address=cd['address'],
            business_type=cd['business_type'], photo=cd['photo'],company_name=cd['company_name'],
            country = country, state = state)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'account/register.html', {'user_form': user_form}) 

def get_state_and_countries(request: HttpRequest) -> HttpResponse:
    data = []
    try:
        response = requests.get(settings.COUNTRIES_AND_STATE_API)
        countries_and_state = response.json()
        #pprint(countries_and_state)
        if not countries_and_state.get('error', True):
            data = countries_and_state.get('data', [])
    except Exception as ex:
        print(ex)
    return JsonResponse({'data': data})

def edit_profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user, data = request.POST)  # type: ignore
        profile_form = ProfileEditForm(instance=request.user.profile, data = request.POST,  # type: ignore
        files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)  # type: ignore
        profile_form = ProfileEditForm(instance=request.user.profile)  # type: ignore
    return render(request, 'account/edit.html', {
        'user_form': user_form, 'profile_form': profile_form
    })