from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Weapon, CustomUser

@receiver(post_save, sender=Weapon)
def notify_users_of_new_weapon(sender, instance, created, **kwargs):
    if created:
        non_admin_users = CustomUser.objects.filter(is_admin=False)
        for user in non_admin_users:
            send_mail(
                subject="New Weapon Added!",
                message=f"Hello {user.username},\n\nA new weapon '{instance.name}' has been added to our catalog. Check it out!",
                from_email="no-reply@fake-spaceshop.com",
                recipient_list=[user.email],
                fail_silently=False,
            )
