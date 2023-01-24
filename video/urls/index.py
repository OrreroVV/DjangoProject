from django.urls import path, include
from video.views.index import index
from video.views import index

urlpatterns = [
    path("", index.index, name="index"),
 ]
