from django.urls import path
from.views import *

urlpatterns=[
    path('register/', registration, name='register')
]
