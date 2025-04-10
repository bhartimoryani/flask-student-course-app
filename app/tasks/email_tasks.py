from time import sleep

from celery_worker import celery


@celery.task
def send_confirmation_email(email):
    sleep(3)
    print(f"Confirmation sent to {email}")
    return f"Confirmation sent to {email}"
