from django.urls import path
from .views import chat_room

app_name = 'chat'

urlpatterns = [
    path('<room>/<int:chat_to>/<int:chat_from>', chat_room),
]