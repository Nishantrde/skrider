from django.urls import path, include
from .views import *

app_name = 'mainapp'

urlpatterns = [path("", index),
               path("galery", galery),
               path("review", reviews),
               path("share_reviews", share_reviews, name = "reviews" ),
               path("cp120", admin_control),
               path("login", login_page)
              ]
 

