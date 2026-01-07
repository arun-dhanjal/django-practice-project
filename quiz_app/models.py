from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.SET_NULL,
        related_name="questions",
        null=True,
        blank=True
    )
    question_text = models.CharField(max_length=200)
    choices = models.JSONField()
    answer = models.CharField(max_length=10)

    def __str__(self):
        return self.question_text
