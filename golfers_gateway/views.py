from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import TeeTimeBookingForm  # Import your form for booking tee time

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

def book_tee_time(request):
    if request.method == 'POST':
        form = TeeTimeBookingForm(request.POST)
        if form.is_valid():
            # Process the booking form
            # This could involve saving the booking details to the database
            # Redirect the user to a confirmation page or back to the homepage
            return redirect('index')
    else:
        form = TeeTimeBookingForm()
    return render(request, 'book_tee_time.html', {'form': form})