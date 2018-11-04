from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    text = "<h1>Homepage!</h1>"
    return HttpResponse(text)
    
def login(request):
    text = "This is login page"
    return HttpResponse(text)
    
def checkHtml(request):
    return render(request, "checkHtml.html", {'today':'home1.png'})