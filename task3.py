from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    if kwargs.get('created', False):
        print("Signal: User created, transaction is active:", transaction.get_connection().in_atomic_block)

# In your views.py

from django.db import transaction

def create_user():
    with transaction.atomic():
        user = User.objects.create(username="test_user")
        print("User saved, transaction is active:", transaction.get_connection().in_atomic_block)
