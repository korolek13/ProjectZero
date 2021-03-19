from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model

class Ice_cream(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    avatar = models.ImageField(blank=True, null=True)
    price = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return str(self.pk)


