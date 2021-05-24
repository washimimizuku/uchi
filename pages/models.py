from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    stub = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)
