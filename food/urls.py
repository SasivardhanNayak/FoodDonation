from django.urls import path
from . import views
urlpatterns= [
    path('',views.login),
    path('index/',views.op),
    path('signin/',views.signin),
    path('signin/signin/',views.signin),
    
]