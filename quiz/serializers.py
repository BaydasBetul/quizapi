from rest_framework import serializers
from .models import Category, Quiz, Question, Answer


class AnswerSerializer(serializers.Serializer):
    class Meta:
        model = Answer
        fields = (
            "answer",
            "is_right"
        )


class QuestionSerializer(serializers.Serializer):

    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            "title",
            "answer",
            "difficulty"
        )


class QuizSerializer(serializers.Serializer):

    question = QuestionSerializer(many=True, write_only=True)

    class Meta:
        model = Quiz
        fields = (
            "title",
            "question",
            "question_count"
        )


class CategorySerializer(serializers.ModelSerializer):

    quiz = QuizSerializer(many=True, write_only=True)
    quiz_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz",
            "quiz_count"
        )

    def get_quiz_count(self, obj):
        return obj.quiz.count()
