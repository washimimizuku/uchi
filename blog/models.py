from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    stub = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)


class Comment(models.Model):
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField('Article')
