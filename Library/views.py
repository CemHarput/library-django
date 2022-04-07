from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from Library.forms import CreateUserForm


def login_Page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registered Successfully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return render(request, 'login.html')


def update(request, pk):
    return HttpResponse('Update Page' + str(pk))


def view(request):
    return HttpResponse('View Page')


def delete(request):
    return HttpResponse('Delete Page')


def home(request):
    return render(request, 'home.html')
