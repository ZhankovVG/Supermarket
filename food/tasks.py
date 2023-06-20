from fresh_food.celery import app
from .servise import send


@app.task
def send_registration_email(user_email):
    send(user_email)