from django.shortcuts import render

from django.http import HttpResponse
from github.r351574nc3.internet_traffic_report.backends.http import lookup_all_routers
from github.r351574nc3.internet_traffic_report.backends.http import lookup_routers_by_name
from github.r351574nc3.internet_traffic_report.backends.http import lookup_top_routers

# Create your views here.
def all_routers(request):
    return HttpResponse(lookup_all_routers(), 'application/json')

def routers_by_name(request, router):
    response = "Testing %s"
    return HttpResponse(lookup_routers_by_name(router), 'application/json')

def continents(request):
    return HttpResponse(lookup_top_routers(), 'application/json')
