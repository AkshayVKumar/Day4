from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"sample.html")

def sample2(request):
    return render(request,"sample1.html")