from django.core.management import BaseCommand

from message_sendler.services import send_mails


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mails()