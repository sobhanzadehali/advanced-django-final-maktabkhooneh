from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from .user import CustomUser


class Profile(models.Model):
    user = models.ForeignKey(
        "accounts.CustomUser", on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
