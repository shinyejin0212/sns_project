from django.urls import path
from .views import *

app_name= 'firstapp'
urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('career/', career, name="career"),
    path('os/', os, name="os"),
    path('dc/', dc, name="dc"),
    path('curriculum/', curriculum, name="curriculum"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name= "create"),
    path('edit/<str:id>', edit, name= "edit"),
    path('update/<str:id>', update, name= "update"),
    path('delete/<str:id>', delete, name= "delete"),
]
