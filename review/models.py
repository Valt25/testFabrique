from django.db import models

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class Question(models.Model):

    class QuestionType(models.TextChoices):
        text = 'text'
        select = 'select'
        checkbox = 'checkbox'

    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=8, choices=QuestionType.choices)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)

    session = models.TextField()