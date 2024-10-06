from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulating a long-running task
    print("Signal handler finished.")

