from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def topic(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            NSTO=tfd.save(commit=False)
            NSTO.save()
            NSWO=wfd.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()
            NSAO=afd.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('topic inserted successfully..............') 
        else:
            return HttpResponse('data is not valid...........')



    return render(request,'topic.html',d)