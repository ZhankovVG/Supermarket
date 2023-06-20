from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Добро пожаловать!',
        'Спасибо за регистрацию!',
        'zhankova.liza.smile@gmail.com',
        [user_email],
        fail_silently=False,
    )
    
    