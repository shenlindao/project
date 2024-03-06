from django.db import models
import uuid

class Page(models.Model):
    MAX_TITLE_LENGTH = 400
    MAX_DESCRIPTION_LENGTH = 2000
    MAX_H1_LENGTH = 100

    id = models.UUIDField (
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.TextField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
    )

    h1 = models.TextField(
        max_length=MAX_H1_LENGTH,
        null=False,
        blank=False
    )

    content = models.TextField(
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    def __str__(self) -> str:
        return self.title