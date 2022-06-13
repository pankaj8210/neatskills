# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


# class SignUpForm(UserCreationForm):
#     name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Name",
#                 "class": "form-control"
#             }
#         ))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder": "Email",
#                 "class": "form-control"
#             }
#         ))
#     number = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Number",
#                 "class": "form-control"
#             }
#         ))
#     module = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Module select",
#                 "class": "form-control"
#             }
#         ))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'number', 'module')
