from django.db import models
from models import File


class FileRefField(models.ForeignKey):
    def __init__(self, **kwargs):
        if 'to' in kwargs:
            del kwargs['to']

        to = File
        kwargs.setdefault("related_name", "+")
        kwargs.setdefault("on_delete", models.PROTECT)
        super(FileRefField, self).__init__(to, **kwargs)
