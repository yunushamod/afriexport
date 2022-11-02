from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse

def notify_user_of_message(request: HttpRequest, user_from_id:int, user_to_id: int):
    """
    Task to send an email notification when a new message come in
    """
    user_from = User.objects.get(id=user_from_id)
    user_to = User.objects.get(id=user_to_id)
    subject = f"{user_from.username.capitalize()} sent you a message"
    message = f'Dear {user_to.first_name.capitalize()}, {user_from.username} sent you a message.\n\n' \
        f"Check it out <a href='{request.build_absolute_uri(reverse('chat:get_messages'))}'>here</a>"
    mail_sent = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_to.email,])
    return mail_sent
