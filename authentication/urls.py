from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [

    url(r'^$', views.CustomHeaderMiddleware.as_view(), name='myurl'),

]
