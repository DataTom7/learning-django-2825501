from django.shortcuts import render
from django.http import Http404
from .models import Driver


def home(request):
    all_drivers = Driver.objects.all()
    return render(request, 'home.html', {
        'drivers': all_drivers,
    })


def driver_detail(request, driver_id):
    try:
        driver = Driver.objects.get(id=driver_id)
    except Driver.DoesNotExist:
        raise Http404('Driver not found')
    return render(request, 'driver_detail.html', {
        'driver': driver,
    })
