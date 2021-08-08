from django.db import models

class Task(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=450)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name