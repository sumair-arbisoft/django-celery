from celery import shared_task
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone
from core.models import UserProfile

User = get_user_model()


@shared_task
def print_hello():
    print("Hello from scheduled task!")


@shared_task
def set_user_is_active(active=True):
    user_id = 2
    try:
        user = User.objects.get(pk=user_id)
        user.is_active = active
        user.save()
        return f"Updated user {user.username} is_active to {active}"
    except User.DoesNotExist:
        return f"User with id {user_id} does not exist"


@shared_task
def verify_user_profile(user_id):
    try:
        user = User.objects.get(pk=user_id)
        user.profile_verified = True
        user.save()
        return f"Verified profile for {user.username}"
    except User.DoesNotExist:
        return f"User with id {user_id} does not exist"


@shared_task
def reset_user_is_pitched():
    try:
        count = 0
        cutoff_date = timezone.now() - timedelta(weeks=2)

        profiles = UserProfile.objects.filter(
            is_pitched_at__lte=cutoff_date,
            is_pitched=True,
            user__is_active=True
        )

        for profile in profiles:
            profile.is_pitched = False
            profile.save()
            print(f"User [{profile.user}] updated.")
            count += 1

        return f"[{count}] User(s) is_pitched column reset successfully."
    except User.DoesNotExist:
        return f"Users with given criteria does not exist."
