from django.shortcuts import render, redirect
from .forms import RegistrationForms, LoginForms
from .models import UzerModel
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _

def logout_views(request):
    logout(request)
    return redirect('blog:my_home')


def login_views(request):
    form_login = LoginForms()
    if request.method == 'POST':
        form_login = LoginForms(data=request.POST)
        if form_login.is_valid():
            uzer = authenticate(username=form_login.cleaned_data['username'],
                                password=form_login.cleaned_data['password'])
            if uzer is not None:
                login(request, uzer)
                return redirect('blog:my_home')
            else:
                form_login.add_error("password", 'Parol yoki username xato!')
    return render(request, 'main/login.html', context={
        'login_views': form_login
    })


def registration_views(request):
    form = RegistrationForms()
    if request.method == 'POST':
        form = RegistrationForms(data=request.POST)
        if form.is_valid():
            user = UzerModel(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                password=make_password(form.cleaned_data['password'])

            )
            user.save()
            return redirect('user:login')
    return render(request, 'main/registration.html', context={
        'registration_form': form
    })
#
#
# def registration_views(request):
#     form = RegistrationForms()
#     if request.method == 'POST':
#         form = RegistrationForms(data=request.POST)
#         if form.is_valid():
#             user = UzerModel(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 password=make_password(form.cleaned_data['password'])
#             )
#             user.save()
#             return redirect('blog:my_home')
#         return render(request, 'main/registration.html', context={
#             'registration_form': form
#         })
