from .models import Order
from django.core.mail import send_mail
from django.conf import settings

def order_created(id: int):
    """
    Task to send an email notification when an order is 
    successfully created.
    """
    order = Order.objects.get(id=id)
    subject = f'Order number. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
        f'You have successfully placed an order.' \
        f'Your order id is: {order.id}'
    mail_sent = send_mail(subject, message, 'admin@portal.afriexporter.com', [order.email])
    return mail_sent

def order_admin_created(id: int):
    """
    Task to send an email notification when an order is successfully created
    """
    order = Order.objects.get(id=id)
    subject = f'Order number. {order.id}'
    message = f'Dear Admin, {order.first_name} has placed an order.' \
        f'The order id is: {order.id}'
    mail_sent = send_mail(subject, message, 'admin@portal.afriexporter.com', [settings.EMAIL_HOST_USER])
    return mail_sent