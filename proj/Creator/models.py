from django.db import models


# Create your models here.
class Creator(models.Model):
    PLATFORMS = [
        ('Instagram', 'Instagram'),
        ('TikTok', 'TikTok'),
        ('UGC', 'User Generated Content')
    ]
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=23, decimal_places=20)
    platform = models.CharField(max_length=20, choices=PLATFORMS)

    def __str__(self):
        return self.name
