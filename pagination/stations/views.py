from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []
    with open('data-398-2018-08-30.csv', encoding='utf-8') as f:
        reader =csv.DictReader(f)
        bus_stations = [{'Name':i['Name'],'Street':i['Street'],'District':i['District']} for i in reader ]
    
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations,len(bus_stations)//1000)
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
