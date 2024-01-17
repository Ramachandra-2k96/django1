from django.shortcuts import render

def home(request):
    return render(request,'classes/index.html',{"param1":'Hello world'})
