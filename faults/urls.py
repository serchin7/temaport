from django.urls import path
from . import views

app_name = 'faultsapp'

urlpatterns = [
    path('', views.tfaults, name='tfaults'),
    path('tAccounts/', views.taccounts, name='taccounts'),
]
