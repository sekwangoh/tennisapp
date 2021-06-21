from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    print(request)
    print(type(request))
    print(dir(request))
    print('-------')
    print(request.POST)
    
    return render(request, 'index.html')


def test(request):
    d = {"name":"sekwang", "age":10}
    return JsonResponse(d)
    #return HttpResponse('hello, world')