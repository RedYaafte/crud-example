from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=50)
    create = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title