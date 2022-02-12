from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField(blank=True, default='')
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']