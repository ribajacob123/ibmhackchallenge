from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from .models import Profile
from .forms import UserLoginForm , UserRegisterForm
# Create your views here.

def login_page(request):
    form = UserLoginForm()
    return render(request, 'web_app/login_page.html',{'form':form})

def reg_page(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "web_app/reg_page.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')




