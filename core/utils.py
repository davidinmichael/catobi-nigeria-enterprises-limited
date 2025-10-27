import json
import os
import random
import string

import requests
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")


def send_email(user_email, subject, template, from_email=DEFAULT_FROM_EMAIL):
    print("Email functio called")
    try:
        email = EmailMultiAlternatives(
            subject=subject,
            body="Your email client doesn't support this content type, view this on another email client or browser.",
            from_email=from_email,
            to=[user_email],
        )
        email.attach_alternative(template, "text/html")
        email.send()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
