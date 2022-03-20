from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="quiz")
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title

    @property
    def question_count(self):
        return self.question.count()


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.DO_NOTHING, related_name="question")
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    Scale = {
        ("0", "Fundamental"),
        ("1", "Beginner"),
        ("2", "Intermediate"),
        ("3", "Advanced"),
        ("4", "Expert"),
    }
    difficulty = models.CharField(max_length=20, choices=Scale)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.DO_NOTHING, related_name="answer")
    updated_date = models.DateTimeField(auto_now=True)
    answer = models.CharField(max_length=200, null=True)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
