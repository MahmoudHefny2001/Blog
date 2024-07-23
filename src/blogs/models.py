from django.db import models

from django_extensions.db.models import TimeStampedModel

from django.contrib.auth.models import User


class Blog(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='user_blogs',
        db_index=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = 'blogs'