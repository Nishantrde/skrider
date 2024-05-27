from django.shortcuts import render
from mainapp.models import *

def index(request):
    return render(request, "index.html")

def galery(request):
    if request.method == "POST":
        return render(request, "galery.html")
    
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


