from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reportCrime/', views.reportCrime, name="reportCrime"),
    path('dashboard/<str:username>', views.dashboard, name="dashboard"),
    path('adminPanel/', views.adminPanel, name="adminPanel"),
    path('deleteData/<int:id>/', views.deleteData, name='deleteData'),
    path('updateDate/<int:id>/', views.updateData, name='updateData'),
    path('updateCase/<int:id>/', views.updateCase, name='updateCase'),
    path('updateInvestigator/<int:id>/', views.updateInvestigator, name='updateInvestigator'),
    path('deleteInvestigator/<int:id>/', views.deleteInvestigator, name='deleteInvestigator'),
    path('deleteCase/<int:id>/', views.deleteCase, name='deleteCase'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]