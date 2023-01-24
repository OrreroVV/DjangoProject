# routing.py
from django.urls import re_path
from video.consumers.showVideos.index import VideoConsumer

websocket_urlpatterns = [
    re_path(r'video/', VideoConsumer.as_asgi()),
    #re_path(r"video/(?P<root_name>\w+)/$", VideoConsumer.as_asgi()),
]