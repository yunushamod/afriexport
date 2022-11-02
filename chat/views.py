from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from .forms import MessageForm
from .models import Messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q 


# Create your views here.

@login_required
def send_message(request: HttpRequest, chat_to: int) -> HttpResponse: #type: ignore
    user_to = get_object_or_404(User, id=chat_to)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Messages.objects.create(user_from=request.user, user_to=user_to, message=cd['message'], read=False)
            return redirect('cart:cart_detail')
    else:
        form = MessageForm()
        return render(request, 'chat/message.html', {'user_to': user_to, 'form': form})

@login_required
def reply_message(request: HttpRequest, parent_message_id: int, user_to_id: int) -> HttpResponse:
    parent_message = get_object_or_404(Messages, id=parent_message_id)
    user_to = get_object_or_404(User, id=user_to_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Messages.objects.create(user_from=request.user, user_to=user_to, message=cd['message'],read=False,
            parent=parent_message)
    return redirect('chat:get_messages')


@login_required
def get_messages(request: HttpRequest) -> HttpResponse:
    messages = Messages.objects.filter(Q(user_to=request.user) | Q(user_from=request.user))
    for message in messages:
        if message.user_to == request.user:
            message.read = True
            message.save()
    form = MessageForm()
    return render(request, 'chat/message_list.html', {'message_list': messages, 'form': form})
