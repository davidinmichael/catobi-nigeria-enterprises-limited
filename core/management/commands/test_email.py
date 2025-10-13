from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from core.utils import send_email
from dotenv import load_dotenv
import os

load_dotenv()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        context = {
            "name": "David",
        }
        template = render_to_string("core/test.html", context)
        send_email("davidinmichael@gmail.com", "Catobi: Confirm Account", template)
        self.stdout.write(self.style.SUCCESS("Email Sent!"))
