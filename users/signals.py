from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from profiles.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwagrs):
    if instance:
        profile = Profile.objects.get_or_create(user=instance)
        profile[0].save()