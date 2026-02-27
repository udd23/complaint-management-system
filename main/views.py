from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('authority_dashboard')
        return redirect('student_dashboard')

    return render(request, 'main/home.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('home')

        user = User.objects.create_user(username=username, password=password)

        # If authority selected → mark as staff
        if role == "authority":
            user.is_staff = True
            user.save()

        login(request, user)

        if user.is_staff:
            return redirect('authority_dashboard')
        else:
            return redirect('student_dashboard')

    return redirect('home')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('authority_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')

    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


def student_dashboard(request):
    return render(request, 'main/student_dashboard.html')


def authority_dashboard(request):
    return render(request, 'main/authority_dashboard.html')