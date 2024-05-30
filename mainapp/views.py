from django.shortcuts import render, redirect
from mainapp.models import *


def index(request):
    photo = Galery.objects.filter(title = "zuluk zigzag roads")
    photos2 = Galery.objects.filter(category = "Sun rising from mountains")

    return render(request, "index.html", {"pic":photo[0], "photos2":photos2[1]})

def galery(request):
    if request.method == "POST":
        if request.POST.get("see") == "second":
            photos = Galery.objects.filter(category = "Sun rising from mountains")
            title = "Sun rising from mountains" 
        else:
            photos = Galery.objects.filter(category = "ZigZag road near Zuluk")
            title = "ZigZag road near Zuluk" 

        return render(request, "galery.html", {"photos":photos, 'title' : title})
    
def reviews(request):
    if request.method == "GET":
        review = Reviews.objects.all()
        print(review)
        return render(request, "review.html", {"reviews" : review})

def share_reviews(request):
    username = ""
    if request.user:
        username = request.user.username[:14]
    if request.method == "POST":
        name = request.POST.get('name')
        review_text = request.POST.get("review")
        ratting = int(request.POST.get("rating"))
        r_image = request.FILES.get('image')
        print(r_image)
        review = Reviews(name=name, review=review_text, rating = ratting, image = r_image)
        review.save()
        return render(request, "share_reviews.html", {"user":username})
    return render(request, "share_reviews.html", {"username":username})

def login_page(request):
    return render(request, "login.html")



