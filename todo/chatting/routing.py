from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
 re_path(r'ws/chatting/conversation/(?P<idcnv>)\w+/$', consumers.Conversation.as_asgi()),   
]