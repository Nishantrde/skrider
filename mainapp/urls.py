from django.urls import path, include
from .views import *

urlpatterns = [path("", index),
               path("galery", galery),
               path("review", reviews),
               path("share_reviews", share_reviews)
              ]


