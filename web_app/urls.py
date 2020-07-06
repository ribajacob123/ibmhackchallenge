from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    #path('user/',views.userpage,name = "userpage"),
    path('login/',views.login_page,name = "login_page"),
    path('reg/',views.reg_page,name = "reg_page"),
    path('logout/', views.logout_view, name="logout"),
    
]