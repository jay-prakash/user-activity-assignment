from django.db import models
from django.contrib.auth.models import AbstractUser
import string
import random


# Generate a random alphanumeric user id
# Takes 1 param (length of the alphanumeric user id)
def generate_userid(length):
    letters_and_digits = string.ascii_uppercase + string.digits
    userid = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return userid


class User(AbstractUser):
    user_id = models.CharField(max_length=9, default=generate_userid(9))
    tz = models.CharField(max_length=50, null=True)


