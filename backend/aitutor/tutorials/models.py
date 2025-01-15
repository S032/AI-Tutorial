from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Manual(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.language.name})"


class Topic(models.Model):
    name = models.CharField(max_length=255)
    manual = models.ForeignKey(Manual, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.manual.name}"


class Tutorial(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.topic.name})"
