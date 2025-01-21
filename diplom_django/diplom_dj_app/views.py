from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserRegister
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


users = []
info = {}


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            if username in users:
                info["error"] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            elif password != repeat_password:
                info["error"] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            elif int(age) < 18:
                info["error"] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            else:
                return redirect('http://127.0.0.1:8000/main_page/')
                #return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    return render(request, 'dj_task/registration_page.html', {'form': form})


def enter(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username in users:
            return redirect('http://127.0.0.1:8000/main_page/')
    return render(request, 'dj_task/enter_page.html')


# Create your views here.
def main_page_f(request):
    return render(request, 'dj_task/main_page.html')


def shop_page_f(request):
    return render(request, 'dj_task/shop_page.html')


def cart_page_f(request):
    return render(request, 'dj_task/cart_page.html')