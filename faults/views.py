from django.shortcuts import render
from .models import Matter


def tfaults(request):
    return render(request, 'faultsapp/tFaults.html')


def taccounts(request):
    return render(request, 'faultsapp/tAccounts.html')


def matter_list(request):
    matters = Matter.objects.all()
    return render(request, 'faultsapp/matter_list.html')
