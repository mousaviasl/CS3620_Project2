from django.db import models

class MadLibStory(models.Model):
    title = models.CharField(max_length=100)
    template = models.TextField()

    def __str__(self):
        return self.title