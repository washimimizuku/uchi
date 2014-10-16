from django.db import models

# Create your models here.
class Page(models.Model):
    title     = models.CharField(max_length=255)
    stub      = models.CharField(max_length=255)
    pub_date  = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)


class Section(models.Model):
    article   = models.ForeignKey('Page')
    title     = models.CharField(max_length=255)
    text      = models.CharField(max_length=200)
    pub_date  = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)


class Tag(models.Model):
    name      = models.CharField(max_length=100)
    pages     = models.ManyToManyField('Page')
