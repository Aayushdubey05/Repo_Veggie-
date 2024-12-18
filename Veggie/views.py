from django.shortcuts import redirect, render
from django.http import Http404,HttpResponse,HttpRequest
from .models import *
# Create your views here.

def veggie(request):
    return render(request , 'base.html')

def home(request):

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        print(receipe_description," ",receipe_name," ",receipe_image)

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description
        )

        return redirect('/receipe/')

    return render(request,'Veggie/receipe.html')