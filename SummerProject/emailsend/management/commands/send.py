import os
from SummerProject.settings import *
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.template.loader import render_to_string


class Command(BaseCommand):

    help = 'Sends an email to the specified email addresses.'

    def add_arguments(self, parser):
        parser.add_argument('subject')
        parser.add_argument('message')
        parser.add_argument('recipient')

    def handle(self, *args, **options):

        message = options['message']
        recipient = options['recipient']

        if os.path.isfile(message):
            try:
                message = open(message).read()
            except (IOError, OSError) as exc:
                raise CommandError('Error reading message file "{}": {}'.format(message, exc))

        options['message'] = message

        try:
            validate_email(recipient)
        except:
            raise CommandError('"{}" is not a valid email address'.format(recipient))

        msg_html = render_to_string('email.html', {'message': options['message']})

        send_mail(
            options['subject'],
            options['message'],
            DEFAULT_FROM_EMAIL,
            [options['recipient']],
            html_message=msg_html,
        )

        self.stdout.write(self.style.SUCCESS('Successfully sent email'))
