from .views import *
from django.conf.urls import url
from django.urls import path

urlpatterns=[path('home/',Home.as_view(),name="home"),
    path('sendMess/',Sendmess.as_view(),name="postMess"),
    path('login/',login.as_view(),name="login"),
    path('details/<str:PID>/<int:Bin>',Details.as_view(),name="detail"),
             ]