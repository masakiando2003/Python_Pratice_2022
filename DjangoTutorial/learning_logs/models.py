from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    """ユーザーが学んでいるトピックを表す"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """モデルの文字列を返す"""
        return self.text


class Entry(models.Model):
    """トピックに関して学んだ具体的なこと"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """モデルの文字列を返す"""
        if len(self.text) > 25:
            return f"{self.text[:25]}..."
        else:
            return self.text