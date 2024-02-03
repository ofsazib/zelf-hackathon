from django.db import models

class Author(models.Model):
    unique_id = models.PositiveBigIntegerField(unique=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.unique_id)


class Content(models.Model):
    creator = models.JSONField()
    content = models.JSONField()

    def __str__(self):
        return str(self.id)
