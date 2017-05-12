from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__ (self):
        return self.question

class Choice(models.Model):
    answer = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__ (self):
        return self.answer
