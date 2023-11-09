from django.shortcuts import render


def tfaults(request):
    return render(request, 'faultsapp/tFaults.html')


def taccounts(request):
    return render(request, 'faultsapp/tAccounts.html')
