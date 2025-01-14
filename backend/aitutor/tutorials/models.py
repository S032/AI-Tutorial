from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=32)


class Manual(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    publication_date = models.DateField()


class Topic(models.Model):
    name = models.CharField(max_length=255)
    manual = models.ForeignKey(Manual, on_delete=models.CASCADE)


class Tutorial(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
