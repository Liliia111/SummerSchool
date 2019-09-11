from django.core.mail import send_mail
from config.settings import DEFAULT_FROM_EMAIL, HOST


def send_reset_email(subject, email, recipient):
    send_mail(subject, email, DEFAULT_FROM_EMAIL, [recipient], html_message=email, fail_silently=False)
