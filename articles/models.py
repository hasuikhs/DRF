from django.db import models
from django.conf import settings

# Create your models here.
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Article(models.Model):
    Height = models.FloatField()
    weight = models.FloatField()
    image = models.ImageField(upload_to=nameFile, max_length=254, blank=True, null=True)
    fat = models.FloatField(blank=True)
    secret = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-pk',]
