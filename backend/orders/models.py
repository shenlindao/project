from django.db import models

class Order(models.Model):
    MAX_NAME_LENGTH = 100
    MAX_EMAIL_LENGTH = 100
    MAX_PHONE_LENGTH = 100

    name = models.TextField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False
    )

    phone = models.TextField(
        max_length=MAX_PHONE_LENGTH,
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
