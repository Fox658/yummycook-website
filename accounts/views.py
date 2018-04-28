from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username =  form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username,password=raw_password)
                user = form.save()
                login(request,user)
                # log the user in
                login(request,user)
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request,user)
            
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
