from django.db import models


class todo(models.Model):
    """docstring for todo"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    done = models.BooleanField()

    def __str__(self):
        return ', '.join([
            self.title,
            self.description,
            str(self.done)
        ])
