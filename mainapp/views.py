from django.shortcuts import render
from mainapp.models import *

def index(request):
    photo = Galery.objects.filter(title = "zuluk zigzag roads")
    return render(request, "index.html", {"pic":photo[0]})

def galery(request):
    if request.method == "POST":
        photos = Galery.objects.filter(category = "ZigZag road near Zuluk")
        return render(request, "galery.html", {"photos":photos, 'title' : 'ZigZag road near Zuluk'})
    
def reviews(request):
    if request.method == "GET":
        review = Reviews.objects.all()
        print(review)
        return render(request, "review.html", {"reviews" : review})

def share_reviews(request):
    if request.method == "POST":
        name = request.POST.get('name')
        review_text = request.POST.get("review")
        review = Reviews(name=name, review=review_text)
        review.save()
        return render(request, "share_reviews.html")
    return render(request, "share_reviews.html")


