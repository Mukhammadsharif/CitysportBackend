from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Subscription, Notification


@receiver(post_save, sender=Subscription)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Create a new notification if the subscription is newly created
        expiration_date = instance.expiration_date
        if expiration_date >= timezone.now().date():
            # Only create a notification if the expiration date is in the future
            Notification.objects.create(
                subscription=instance,
                text=f"The subscription '{instance.name}' is expiring on {expiration_date}."
            )
    else:
        # Update the notification if the subscription is updated
        expiration_date = instance.expiration_date
        notification = Notification.objects.filter(subscription=instance).first()
        if expiration_date >= timezone.now().date():
            # Update the notification if the expiration date is in the future
            if notification:
                notification.text = f"The subscription '{instance.name}' is expiring on {expiration_date}."
                notification.save()
            else:
                Notification.objects.create(
                    subscription=instance,
                    text=f"The subscription '{instance.name}' is expiring on {expiration_date}."
                )
        else:
            # Delete the notification if the expiration date is in the past
            if notification:
                notification.delete()
