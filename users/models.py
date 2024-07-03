from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    """Custom user Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENG = "en"
    LANGUAGE_HINDI = "hind"
    LANGAUGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, "English"),
        (LANGUAGE_HINDI, "Hindi"),
        (LANGAUGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_INR = "inr"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_INR, "Inr"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=4, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=5, blank=True)
    superhost = models.BooleanField(default=False)
