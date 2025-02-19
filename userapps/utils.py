from django.core.mail import send_mail
from django.conf import settings

def send_Email(email):
    subject = "Welcome on-board"
    body = '''
        Dear user,
        Thank you for setting an account with us.

        This is a welcome message from the dev team.
    '''
    send_mail(
    subject,
    body,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)

