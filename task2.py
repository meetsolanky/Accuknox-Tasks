import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")


def create_user():
    print(f"Caller running in thread: {threading.current_thread().name}")
    user = User.objects.create(username="test_user")