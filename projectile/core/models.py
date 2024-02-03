from django.db import models

class Author(models.Model):
    unique_id = models.PositiveBigIntegerField(unique=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.unique_id)


class Content(models.Model):
    unique_id = models.PositiveBigIntegerField(unique=True)
    data = models.JSONField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.unique_id)
