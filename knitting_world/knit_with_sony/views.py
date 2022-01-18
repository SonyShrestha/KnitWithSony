from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def item_index_by_number(request,item):
    return HttpResponse(item)
    
def item_index(request,item):
    if item=="shoes":
        responseText= "This is for shoes"
    elif item=="sweater":
        responseText= "This is for sweater"
    elif item=="topi":
        responseText= "This is for topi"
    else:
        return HttpResponseNotFound("This item is not prepared yet")
    return HttpResponse(responseText)