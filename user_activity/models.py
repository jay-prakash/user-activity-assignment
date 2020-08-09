from django.db import models
from accounts.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone


class UserActivity(models.Model):
    user = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Activities'


# Django signal for add user activity start time while login
@receiver(user_logged_in, sender=User)
def login_signal(sender, request, user, **kwargs):
    UserActivity.objects.create(user=user, start_time=timezone.now())


# Django signal for updating user activity end time while logout
@receiver(user_logged_out, sender=User)
def logout_signal(sender, request, user, **kwargs):
    user_activity = UserActivity.objects.filter(user=user).last()
    user_activity.end_time = timezone.now()
    user_activity.save()