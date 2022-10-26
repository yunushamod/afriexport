from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User

# Create your views here.

def chat_room(request: HttpRequest, chat_to: int, chat_from: int) -> HttpResponse:
    try:
        user_to = get_object_or_404(User, id=chat_to)
        user_from = get_object_or_404(User, id=chat_from)
    except:
        return HttpResponseNotFound()
    return render(request, 'chat/room.html', {'user_to': user_to, 'user_from': user_from})
