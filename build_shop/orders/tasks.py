from celery import shared_task
# from celery.task.schedules import crontab
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    # order = Order.objects.get(id=order_id)
    # subject = 'Order nr. {}'.format(order.id)
    # message = 'Dear {},\n\nYou have successfully placed an order.\
    #                                 Your order id is {}.'.format(order.name,order.id)
    # mail_sent = send_mail(subject,
    #                       message,
    #                       'nhquan0911@gmail.com',
    #                       ['quanbadao0@gmail.com'])
    # return mail_sent
    for i in range(10):
        print(i)
    return "đ"

