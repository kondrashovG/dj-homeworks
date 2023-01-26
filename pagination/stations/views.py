from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
# from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page = request.GET.get('page')
    if not page:
        page = 1
    else:
        page = int(page)
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        # reader = csv.DictReader(csvfile)
        # p = Paginator(reader, 10)
        # print(p.count)
        page_list = []
        num_row = 0
        last_row = page * 10
        first_row = last_row - 9
        print(first_row, last_row)
        for row in csv.DictReader(csvfile):
            num_row += 1
            if num_row in range(first_row, last_row+1):
                page_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    last_page = int(num_row / 10 + 1)
    context = {
         'bus_stations': page_list,
         'page': {
            'has_previous': page > 1,
            'previous_page_number': page - 1,
            'number': page,
            'has_next': page < last_page,
            'next_page_number': page + 1
         },
    }
    return render(request, 'stations/index.html', context)
