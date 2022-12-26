from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('red/',red,name='red'),
    path('green/',green,name='green'),
]
