from django.db import models
from uuid import uuid4


class Application(models.Model):
    """Contains external source that would call API"""

    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def generate_key():
        return uuid4()

    key = models.CharField(max_length=200, unique=True, default=generate_key)
