from django.core import mail
from django.core.management import CommandError, call_command
import pytest
from SummerProject.settings import *


@pytest.fixture(autouse=True)
def email_backend_setup(settings):
    settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


def test_noargs():
    pytest.raises(CommandError, call_command, 'send')


def test_bad_address():
    pytest.raises(CommandError, call_command, 'send', 'subject', 'message', 'lalala')


def test_outbox():
    call_command('send', 'subject', 'message', 'user1290876@gmail.com')
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'subject'
