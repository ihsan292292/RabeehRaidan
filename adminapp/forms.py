# app1/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class SuperuserLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_superuser:
            raise forms.ValidationError(
                "This account doesn't have admin privileges.",
                code='no_superuser',
            )
