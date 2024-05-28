from django.shortcuts import render
from mainapp.models import *

def index(request):
    # titl
    photo = Galery.objects.filter(title = "zuluk zigzag roads")
    photos2 = Galery.objects.filter(category = "Sun set view from mountain view")

    return render(request, "index.html", {"pic":photo[0], "photos2":photos2[1]})

def galery(request):
    if request.method == "POST":
        if request.POST.get("see") == "second":
            photos = Galery.objects.filter(category = "Sun set view from mountain view")
            title = "Sun set view from mountain view" 
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
    if request.method == "POST":
        name = request.POST.get('name')
        review_text = request.POST.get("review")
        ratting = int(request.POST.get("rating"))
        review = Reviews(name=name, review=review_text, rating = ratting)
        review.save()
        return render(request, "share_reviews.html")
    return render(request, "share_reviews.html")


