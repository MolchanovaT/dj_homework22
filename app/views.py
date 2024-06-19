from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from app import settings


def index(request):
    return redirect(reverse(bus_stations))


CONTENT = []
with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        CONTENT.append(row)


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    current_page = page_number
    next_page_url = f"{reverse('bus_stations')}?page={current_page + 1}"
    if current_page == 1:
        prev_page_url = None
    else:
        prev_page_url = f"{reverse('bus_stations')}?page={current_page - 1}"
    print(next_page_url)
    print(prev_page_url)
    return render(request, 'index.html', context={
        'bus_stations': page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
