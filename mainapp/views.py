from django.shortcuts import render
from mainapp.models import *


def index(request):
    headings = Webcontent.objects.all()
    photos = []
    for heading in headings:
        print(heading)
        photos.append(Galery.objects.filter(title = str(heading))[0])
    print(photos[0])
    return render(request, "index.html", {"photos": photos})

def galery(request):
    if request.method == "POST":
        if request.POST.get("galery"):
            content = str(request.POST.get("galery"))
            photos = Galery.objects.filter(category = content)
            title = "Sun rising from mountains" 
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
        review = Reviews(name=name, review=review_text, rating = ratting, image = r_image)
        review.save()
        return render(request, "share_reviews.html", {"user":username})
    return render(request, "share_reviews.html", {"username":username})

def login_page(request):
    return render(request, "login.html")

def admin_control(request):
    
    if request.method == "POST":
        if request.POST.get("add_category"):
            admin_category = request.POST.get("add_category")
            admin_description = request.POST.get("description")
            obj1 = Webcontent(heading = admin_category, description = admin_description)
            obj2 = Galery(title = admin_category, category = admin_category)
            obj1.save()
            obj2.save()

        if request.POST.get("category"):
            print(request.POST.get("category"))
            admin_title = request.POST.get("category")
            admin_image = request.FILES.get('image')
            Galery.objects.filter(image=None).delete()
            obj = Galery(title = admin_title, category = admin_title, image = admin_image)
            obj.save()

    headings = Webcontent.objects.all()
    photos = []
    for heading in headings:
        photos.append(Galery.objects.filter(title = str(heading))[0])
    return render(request, "admin_control.html", {"photos": photos})

