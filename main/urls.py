from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reportCrime/', views.reportCrime, name="reportCrime"),
    path('dashboard/<str:username>', views.dashboard, name="dashboard")
]