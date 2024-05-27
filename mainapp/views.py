from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def galery(request):
    if request.method == "POST":
        return render(request, "galery.html")


