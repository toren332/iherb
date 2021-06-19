from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


class Article(models.Model):
    name = models.TextField()
    link = models.URLField()
    rating = models.IntegerField()


class Drug(models.Model):
    name = models.TextField()
    articles = models.ManyToManyField(Article, blank=True, null=True)


class Bad(models.Model):
    name = models.TextField()
    qcode = models.CharField(max_length=32)
    count = models.TextField()
    img = models.URLField()
    link = models.URLField()
    info = models.TextField(blank=True, null=True)
    categories = ArrayField(models.TextField(), blank=True, null=True)
    drugs = models.ManyToManyField(Drug, blank=True, null=True)
    drug_count = models.JSONField(default=dict, blank=True, null=True)
