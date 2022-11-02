from .models import OrderItem
from django.core.mail import send_mail
from django.conf import settings

def order_created(id: int):
    """
    Task to send an email notification when an order is 
    successfully created.
    """
    order_item = OrderItem.objects.get(id=id)
    subject = f'Order number. {order_item.order.id}' #type: ignore
    message = f'Dear {order_item.order.first_name},\n\n' \
        f'You have successfully placed an order for {order_item.product.name}.' \
        f'Your order id is: {order_item.order.id}' #type: ignore
    mail_sent = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [order_item.order.email])
    return mail_sent

def order_admin_created(id: int):
    """
    Task to send an email notification when an order is successfully created
    """
    order_item = OrderItem.objects.get(id=id)
    subject = f'Order number. {order_item.order.id}' #type: ignore
    message = f'Dear Admin, {order_item.order.first_name} has placed an order.' \
        f'The order id is: {order_item.order.id}' #type: ignore
    mail_sent = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])
    return mail_sent

def order_owner_created(id: int):
    """Task to send an email notification when an order has been successfully created to the owner"""
    order_item = OrderItem.objects.get(id=id)
    subject = f'{order_item.order.first_name} has ordered {order_item.quantity}  {order_item.product.name} from your store'
    message = f'Dear {order_item.product.user.first_name} {order_item.order.first_name} has ordered {order_item.quantity}  {order_item.product.name} from your store'
    mail_sent = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [order_item.product.user.email,])