from django.urls import path
from . import views
urlpatterns= [
    path('index',views.index,name="index"),
    path('',views.Login,name="login"),
    path('signup',views.signup,name="signup"),
    path('food_donate',views.donate_food,name="food_donate"),
    path('cloth_donate',views.donate_cloth,name="cloth_donate"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('placerequest',views.placerequest,name="placerequest"),
    path("profile",views.profile,name="profile"),
    path("peding_request",views.pending_request,name="pending_request")
    
]
