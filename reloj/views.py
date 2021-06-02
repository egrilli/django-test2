from django.shortcuts import render, HttpResponse
from time import localtime, strftime


def reloj(request):
    context = {
        "date": strftime("%d-%B-%Y", localtime()),
        "time":strftime("%H:%M %S %p ", localtime())
    }
    return render(request,'reloj.html', context)
    