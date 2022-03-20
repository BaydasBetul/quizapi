from .models import Category, Quiz, Question, Answer
from django.contrib import admin
import nested_admin
from django.contrib.admin import TabularInline, StackedInline, site
from .models import Answer, Question, Quiz,Category

class AnswerInline(nested_admin.NestedStackedInline):
    model =Answer
    extra = 4

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]
    
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)


