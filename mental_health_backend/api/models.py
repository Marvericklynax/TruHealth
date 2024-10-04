from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)  # Make it nullable
    content = models.TextField()
    category = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
