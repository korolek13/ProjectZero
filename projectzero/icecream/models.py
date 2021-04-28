from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Ice_cream(models.Model):
    name = models.CharField(
        verbose_name = 'имя',
        max_length=40,
        help_text = 'Название мороженного'    
    )
    description = models.TextField()
    avatar = models.ImageField(blank=True, null=True)
    price = models.IntegerField()
    rating = models.IntegerField()
    users = models.ManyToManyField(User)
    class Meta:
        ordering = ['-id']


    def __str__(self):
        return str(self.pk)

class Follow(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        related_name = 'follower',
    )
    author = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        related_name = 'following',
    )
