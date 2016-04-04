from django.shortcuts import *
from django.shortcuts import render
from django.template import RequestContext
# Create your views here.

def index(request):
    return render(request, 'findlocation/home.html')

def getlocation(request):
    if request.method == "GET":
        print(request.GET.get('input'))
        return render_to_response('findlocation/streetLocation.html',{'success': request.GET.get('input')},context_instance=RequestContext(request))
    else:
        return render_to_response('findlocation/streetLocation.html',{},context_instance=RequestContext(request))