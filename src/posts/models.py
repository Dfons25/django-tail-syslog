from django.db import models

# Create your models here.
# Data object
# Corresponds to database structure
class Pub(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title
