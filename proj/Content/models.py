from django.db import models
from django.db import models

from Creator.models import Creator


class Content(models.Model):
    creator = models.ForeignKey(Creator,on_delete=models.CASCADE)
    url = models.URLField(max_length=200)


    def __str__(self):
        return f" Content by:  {self.creator}  - {self.url}"
