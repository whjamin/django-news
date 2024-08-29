from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    date = models.CharField(max_length=255)

    def __str__(self):
        return self.title