from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed  = models.BooleanField(default=False , blank=True , null= True)

    def __str__(self):
        return self.title