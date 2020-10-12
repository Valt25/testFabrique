from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from review.models import Review, Question, Answer


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'start_date', 'end_date', 'description')
        read_only_fields = ('id',)


class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'start_date', 'end_date', 'description')
        read_only_fields = ('start_date', 'id')


class CreateQuestionSerializer(serializers.ModelSerializer):
    review_id = serializers.PrimaryKeyRelatedField(source='review', queryset=Review.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'text', 'type', 'review_id')
        read_only_fields = ('id',)


class UpdateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'type', 'review_id')
        read_only_fields = ('id', 'review_id')


class CreateAnswerSerializer(serializers.ModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(source='question', queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ('answer_text', 'question_id')

    def validate(self, attrs):
        print(attrs)
        answer = Answer.objects.filter(question_id=attrs['question'], session=self.context['session'])
        if answer:
            raise ValidationError('It is impossible to answer the same question twice')
        return attrs

    def save(self, **kwargs):
        super().save(session=self.context['session'])
