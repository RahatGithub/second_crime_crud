from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('login-as-investigator/', views.loginAsInvestigator, name="loginAsInvestigator"),
    path('register/', views.register, name="register"),
    path('register-as-investigator/', views.registerAsInvestigator, name="registerAsInvestigator"),
    path('logout/', views.logout, name="logout"),
]