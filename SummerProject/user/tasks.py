from celery.decorators import task
from celery.utils.log import get_task_logger

from user.email import send_reset_email

logger = get_task_logger(__name__)


@task(name="send_reset_email_task")
def send_reset_email_task(subject, email, recipient):
    logger.info("Sent email")
    return send_reset_email(subject, email, recipient)
