from django.contrib.auth.middleware import RemoteUserMiddleware
from django import forms
from authentication.models import Post

class HomeForm(forms.ModelForm,RemoteUserMiddleware):

        user ="user login"

        class Meta:
                model = Post
                fields = '__all__'



