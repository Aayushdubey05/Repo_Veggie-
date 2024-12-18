from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,Http404
# Create your views here.


def home(request):
    peoples=[
    {'name': 'Rohan Dol', 'age': 34},
    {'name': 'Aayush Dubey', 'age': 24},
    {'name': 'Manoj', 'age': 54},
    {'name': 'Jury', 'age': 14}
    ]
    x = '24'
    return render(request, 'index.html', context= {'peoples': peoples})

def support(request):
    return HttpResponse("<h1>I am here to support u guys</h1>")