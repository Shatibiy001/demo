from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            name=instance.username.title(),
            username=instance.username,
            email=instance.email,
        )

        # Optional: send welcome email
        send_mail(
            'Welcome to the Platform!',
            f'Hi {instance.username},\n\nYour account is ready!',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=True,
        )
        
