from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint as rnd
from django.contrib.auth import logout

def index(request):
    if not request.user.is_authenticated :
        redirect(reverse('firstapp:user_login'))
    else :
        logout(request)
        return HttpResponse(f'{rnd(1000, 10000)}')


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.urls import reverse

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('firstapp:index'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})



