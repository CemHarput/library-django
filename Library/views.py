from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from Library.forms import CreateUserForm


def login(request):
    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


def update(request, pk):
    return HttpResponse('Update Page' + str(pk))


def view(request):
    return HttpResponse('View Page')


def delete(request):
    return HttpResponse('Delete Page')


def home(request):
    return render(request, 'home.html')
