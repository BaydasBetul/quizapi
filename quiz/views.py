from django.shortcuts import render
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer
from .models import Question, Answer, Quiz, Category
from rest_framework import generics, viewsets
from rest_framework.views import APIView
# Create your views here.


class QuizListView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizRead(generics.ListAPIView):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    def get_queryset(self):
        category = self.kwargs['category'].title()
        return Quiz.objects.filter(category_name=category)


class QuestionRead(generics.ListAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get_queryset(self):
        quiz = self.kwargs['quiz'].title()
        return Question.objects.filter(category_name=quiz)
