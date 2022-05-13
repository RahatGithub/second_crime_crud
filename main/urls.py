from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reportCrime/', views.reportCrime, name="reportCrime"),
    path('dashboard/<str:username>', views.dashboard, name="dashboard"),
    # path('adminPanel/<str:username>', views.adminPanel, name="adminPanel"),
    path('adminPanel/', views.adminPanel, name="adminPanel"),
    path('deleteData/<int:id>/', views.deleteData, name='deleteData'),
    path('updateDate/<int:id>/', views.updateData, name='updateData')
]