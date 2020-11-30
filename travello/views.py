from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
#superuser: mohit
#password : 1234
def index (request):
    #return HttpResponse ("<h1>hello world</h1>");
    """
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc='the city never sleeeps'
    dest1.price=800
    dest1.img='1.jpg'
    dest1.offer= True

    dest2=Destination()
    dest2.name='hydrabad'
    dest2.desc='beautiful ciy'
    dest2.price=1000
    dest2.img='2.jpg'
    dest2.offer= False
    """

   # dests=[dest1,dest2]
    dests=Destination.objects.all()
    return render(request, 'index.html',{'dests': dests})
