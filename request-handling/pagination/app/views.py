import urllib

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

import csv

from app import settings
from functionCSV import  function_csv2


def index(request):
    return redirect(reverse(bus_stations))



def bus_stations(request):
    current_page = 1
    next_page_url = 'write your url'
    content = function_csv2()
    page_number = int(request.GET.get('page',1))
    paginator = Paginator(content, settings.ITEMS_PER_PAGE)
    page_obj = paginator.get_page(page_number)
    params = urllib.parse.urlencode({'page': page_obj.next_page_number()})
    url = reverse('bus_stations')
    if page_obj.has_next() == True:
        next_page_url = f'{url}?{params}'
    elif page_obj.has_next() == False:
        next_page_url = None
    if page_obj.has_previous() == True:
        params2 = urllib.parse.urlencode({'page': page_obj.previous_page_number()})
        current_page = page_obj.number
        prev_page_url = f'{url}?{params2}'
    elif page_obj.has_previous() == False:
        prev_page_url = None
    return render(request, 'index.html', context={
            'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'},
                             {'Name': page_obj.object_list[0][0], 'Street': page_obj.object_list[0][1], 'District': page_obj.object_list[0][2]},
                             {'Name': page_obj.object_list[1][0], 'Street': page_obj.object_list[1][1], 'District': page_obj.object_list[1][2]},
                             {'Name': page_obj.object_list[2][0], 'Street': page_obj.object_list[2][1], 'District': page_obj.object_list[2][2]},
                             {'Name': page_obj.object_list[3][0], 'Street': page_obj.object_list[3][1], 'District': page_obj.object_list[3][2]},
                             {'Name': page_obj.object_list[4][0], 'Street': page_obj.object_list[4][1], 'District': page_obj.object_list[4][2]},
                             {'Name': page_obj.object_list[5][0], 'Street': page_obj.object_list[5][1], 'District': page_obj.object_list[5][2]},
                             {'Name': page_obj.object_list[6][0], 'Street': page_obj.object_list[6][1], 'District': page_obj.object_list[6][2]},
                             {'Name': page_obj.object_list[7][0], 'Street': page_obj.object_list[7][1], 'District': page_obj.object_list[7][2]},
                             {'Name': page_obj.object_list[8][0], 'Street': page_obj.object_list[8][1], 'District': page_obj.object_list[8][2]},
                             {'Name': page_obj.object_list[9][0], 'Street': page_obj.object_list[9][1], 'District': page_obj.object_list[9][2]},
                             {'Name': page_obj.object_list[10][0], 'Street': page_obj.object_list[10][1], 'District': page_obj.object_list[10][2]},
                             {'Name': page_obj.object_list[11][0], 'Street': page_obj.object_list[11][1], 'District': page_obj.object_list[12][2]},
                             {'Name': page_obj.object_list[13][0], 'Street': page_obj.object_list[13][1], 'District': page_obj.object_list[13][2]},
                             {'Name': page_obj.object_list[14][0], 'Street': page_obj.object_list[14][1], 'District': page_obj.object_list[14][2]}
                             ],

            'current_page': current_page,
            'prev_page_url': prev_page_url,
            'next_page_url': next_page_url,
        })

