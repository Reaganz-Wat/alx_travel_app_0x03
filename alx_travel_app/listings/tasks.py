# from celery import shared_task
# from django.core.mail import send_mail

# @shared_task
# def send_booking_confirmation_email(user_email, booking_id):
#     subject = "Booking Confirmation"
#     message = f"Your booking with ID {booking_id} has been confirmed."
#     send_mail(
#         subject,
#         message,
#         "no-reply@alxtravel.com",
#         [user_email],
#         fail_silently=False,
#     )
#     return f"Email sent to {user_email} for booking {booking_id}"



from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings  # import settings to get EMAIL_HOST_USER

@shared_task
def send_booking_confirmation_email(user_email, booking_id):
    subject = "Booking Confirmation"
    message = f"Your booking with ID {booking_id} has been confirmed."
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Use your Gmail address here
        [user_email],
        fail_silently=False,
    )
    return f"Email sent to {user_email} for booking {booking_id}"