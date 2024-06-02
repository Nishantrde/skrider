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
            return render(request, "galery.html", {"photos":photos, 'title' : photos[0].category})
    
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
            obj2 = Galery(title = admin_category, category = admin_category, description = admin_description)
            obj1.save()
            obj2.save()

        if request.POST.get("category"):
            admin_title = request.POST.get("category")
            admin_image = request.FILES.get('image')
            obj1 = Webcontent.objects.filter(heading = admin_title)
            Galery.objects.filter(image=None).delete()
            if obj1:
                des = obj1[0].description
            else:
                des = ""
            obj = Galery(title = admin_title, category = admin_title, image = admin_image, description = des)
            obj.save()
        
        if request.POST.get("admin_add"):
            obj = Contacts.objects.first()
            if request.POST.get("name") != "":
                name = request.POST.get("name")
                obj.name = name
            if request.POST.get("email") != "":
                email = request.POST.get("email")
                obj.email = email
            if request.POST.get("Ph_no.") != "":
                phn = request.POST.get("Ph_no.")
                obj.phone_number = phn   
            obj.save()


    headings = Webcontent.objects.all()
    photos = []
    for heading in headings:
        photos.append(Galery.objects.filter(title = str(heading))[0])
        obj = Contacts.objects.first()
        name = obj.name
        email = obj.email
        phn = obj.phone_number
    return render(request, "admin_control.html", {"photos": photos, "name":name, "email":email, "phn":phn})

