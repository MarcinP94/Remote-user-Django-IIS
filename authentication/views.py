from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth.middleware import RemoteUserMiddleware


def home(request):
    return render(request, 'authentication/home.html')

def detail(request):
    return render(request,)

class CustomHeaderMiddleware(TemplateView,RemoteUserMiddleware):

    header = 'REMOTE_USER'


    def render_to_response(self, context, **response_kwargs):
        response = HttpResponse(content_type='text/plain')
        response.write("logowanie %s" % (self.request.META['REMOTE_USER']))
        #request.META['REMOTE_USER']
        return  response


