from django.urls import path
from .views import send_message, get_messages, reply_message

app_name = 'chat'

urlpatterns = [
    path('room/<int:chat_to>/', send_message, name='send_message'),
    path('room/reply/<int:parent_message_id>/<int:user_to_id>/', reply_message, name='reply'),
    path('room/messages/all/', get_messages, name='get_messages')
]