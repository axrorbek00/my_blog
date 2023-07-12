from django import forms
from django.core.exceptions import ValidationError
from .models import UzerModel
from django.utils.translation import gettext_lazy as _


class LoginForms(forms.Form):
    username = forms.CharField(max_length=25, label=_("Username"), min_length=3, widget=forms.TextInput(attrs={
        'placeholder': _('Username')
    }))
    password = forms.CharField(max_length=16, label=_("Password"), min_length=6, widget=forms.PasswordInput(attrs={
        'placeholder': _('Password')
    }))


class RegistrationForms(forms.Form):
    username = forms.CharField(max_length=100, label=_("Username"), min_length=3, widget=forms.TextInput(attrs={
        'placeholder': _('Username')
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Youremailname@gmail.com'
    }))
    first_name = forms.CharField(label=_("First name"), max_length=25)
    last_name = forms.CharField(label=_("Last name"), max_length=25)
    password = forms.CharField(label=_("Password"), max_length=16, min_length=6, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label=_("Confirm password"), max_length=16, min_length=6,
                                       widget=forms.PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError(_("The passwords are not thr some!"))
        else:
            return self.cleaned_data

    def clean_user(self):
        user = UzerModel.objects.get(username=self.cleaned_data['username'])
        if user:
            raise ValidationError(_("This username is busy"))
        else:
            return self.cleaned_data
