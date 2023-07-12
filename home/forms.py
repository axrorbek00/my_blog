from django import forms
from ckeditor.fields import RichTextFormField
from django.utils.translation import gettext_lazy as _


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=100, label=_('title'), widget=forms.TextInput(attrs={
        'placeholder': _("Post title")
    }))

    body = RichTextFormField(label=_('Post body'))

    img = forms.ImageField(widget=forms.FileInput(), label=_('Post image'))
