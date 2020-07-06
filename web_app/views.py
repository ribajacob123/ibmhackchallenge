from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import UserRegisterForm , UserLoginForm
#from .filters import OrderFilter
#from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.
#@unauthenticated_user
def login_page(request):
	form = UserLoginForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if not user:
			raise forms.ValidationError('This user does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')
			if not user.is_active:
				raise forms.ValidationError('This user is not active')
		if user is not None:
			login(request, user)
			return render(request,'web_app/dashboard.html')
		else:
			messages.info(request, 'Username OR password is incorrect')
	return render(request, 'web_app/login_page.html',{'form':form})

def reg_page(request):
	next = request.GET.get('next')
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('login/')
	context = {'form':form}
	return render(request, "web_app/reg_page.html", context)
			

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url = 'login/')
def home(request):

	return render(request ,"web_app/dashboard.html",{})

