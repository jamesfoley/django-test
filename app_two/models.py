from django.db import models

from file.fields import FileRefField


class ModelTwo(models.Model):
    item = FileRefField(
        blank=True,
        null=True
    )
