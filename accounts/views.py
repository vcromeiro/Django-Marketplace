from django.shortcuts import render, redirect #, HttpResponseRedirect
from django.urls import reverse
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
    )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def redirectHome(request):
    return redirect('home:home')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        ############# ADIÇÃO #################
        else:
            return render(request, 'accounts/reg_form.html', {'form': form})
        ######################################
    else:
        form = RegistrationForm()
            
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

#@login_required     
def view_profile(request, pk=None):
    if pk:
        user =  User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

#@login_required  
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    ### ONDE FALTA O ELSE ###
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

#@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:change_password'))
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)