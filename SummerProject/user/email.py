from django.core.mail import send_mail
from config.settings import DEFAULT_FROM_EMAIL, HOST


def send_reset_email(subject, email, recipient):
    try:
        send_mail(subject, email, DEFAULT_FROM_EMAIL, [recipient], html_message=email, fail_silently=False)
    except Exception as e:
        print(str(e))
