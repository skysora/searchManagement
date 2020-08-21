from django import forms

from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.utils.html import conditional_escape


class loginForm(forms.Form):
    user_name = forms.CharField(label="username", max_length=20)
    password = forms.CharField(
        label="password", max_length=20, widget=forms.PasswordInput)







